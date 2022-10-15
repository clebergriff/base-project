from functools import reduce
from operator import and_, or_
from api.classes.authenticated_view import AllowPostOnlyPermission, AuthenticatedView
from api.helpers.response_helpers import build_bulk_response
from api.models import Article, Profile
from api.serializers import ArticleSerializer, ProfileSerializer
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.auth.models import User
from rssfeed.pagination import CustomPagination
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token


class AuthenticationView(GenericAPIView):
    # get token for user
    def post(self, request):
        try:
            user = User.objects.get(username=request.data['username'])
            if user.check_password(request.data['password']):
                token, created = Token.objects.get_or_create(user=user)
                return Response(status=status.HTTP_200_OK, data={'token': token.key})
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'Invalid password'})
        except User.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'Invalid credentials'})


class ArticleViewSet(AuthenticatedView):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = CustomPagination

    def post(self, request, format=None):
        is_bulk = isinstance(request.data, list)
        # check if the request is a single article or a list of articles
        serializer = self.get_serializer(data=request.data, many=is_bulk)
        if serializer.is_valid():
            response = serializer.save()
            # count how many of each status code we have
            # and return a count of each
            if is_bulk:
                bulk_response = build_bulk_response(response)
                return Response(status=200, data=bulk_response)
            else:
                return Response(status=response.status_code, data=response.data)
        return Response(status=400, data=serializer.errors)

    def get(self, request, format=None):
        search = request.GET.get('search', None)
        language = request.GET.get('language', None)
        if language is not None:
            queryset = self.filter_queryset(
                self.queryset.filter(language=language))
        if search is not None:
            # a result should have all the words from the search
            # for example: search = "hello world"
            # a result should have both "hello" and "world" anywhere in the title
            # or in the description
            keywords = search.split()
            # keywords in an array of words that might be in title or description
            # get all Articles that has at least one of the keywords in the title or description
            # counting titles and descriptions matched, an Article must meet all the keywords

            queryset = self.filter_queryset(
                self.queryset.filter(reduce(or_, [Q(title__icontains=keyword) | Q(
                    description__icontains=keyword) for keyword in keywords]))
            )

            # filter out Articles that don't have all the keywords
            queryset = queryset.filter(reduce(and_, [Q(title__icontains=keyword) | Q(
                description__icontains=keyword) for keyword in keywords]))

        else:
            queryset = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        return Response(status=200, data=data)

    def filter_queryset(self, queryset):
        queryset = queryset.order_by('-published_date')
        return queryset


class GamerfetaminaViewSet(AuthenticatedView):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = CustomPagination

    def get(self, request, format=None):
        url = 'https://rss.tecmundo.com.br/feed'
        urls = [
            'tecmundo',
            'olhardigital',
            'globo',
            'xbox'
        ]

        if urls is not None:
            # urls is an array of strings
            # we need to filter with only urls that have one of more strings from urls in it
            queryset = self.filter_queryset(
                self.queryset.filter(url__icontains=urls[0]))
            for url in urls[1:]:
                queryset = queryset | self.filter_queryset(
                    self.queryset.filter(url__icontains=url))
        else:
            queryset = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        return Response(status=200, data=data)

    def filter_queryset(self, queryset):
        queryset = queryset.order_by('-published_date')
        return queryset


class HelloView(AuthenticatedView):

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class UserView(AllowPostOnlyPermission):

    def get(self, request, **kwargs):
        # check if username exists. If it does, return the user User
        # if it doesn't, return 404
        # username comes from the url
        username = kwargs['username'] if 'username' in kwargs else None

        if username is not None:
            try:
                user = Profile.objects.get(user__username=username)
                serializer = ProfileSerializer(user)
                return Response(status=200, data=serializer.data)
            except Exception as e:
                return Response(status=404, data={'error': str(e)})
        else:
            user = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        if username == '' or password == '':
            return Response({
                'message': 'username and password are required'
            }, status=400)

        try:
            # create a new User and save it
            new_user = User.objects.create_user(
                username=username, password=password)
            return Response({
                'message': 'User created successfully'
            }, status=201)
        except Exception as e:

            # if exception is a unique constraint violation, show "username already exists"
            # otherwise, show the exception
            if 'UNIQUE constraint failed' in str(e):
                error_message = 'Username already exists'
            else:
                error_message = str(e)

            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': error_message})
