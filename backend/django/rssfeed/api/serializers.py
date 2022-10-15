from rest_framework import serializers
from .models import Article, Profile, User
from rest_framework.response import Response


class ArticleSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        try:
            try:
                article = Article.objects.get(url=validated_data['url'])
                return Response(status=200, data={'info': f'Article {article.url} already exists'})
            except Article.DoesNotExist:
                article = Article.objects.create(**validated_data)
                return Response(status=201, data={'info': 'Article created - {}'.format(article.url)})
        except Exception as e:
            print(e)

    class Meta:
        model = Article
        fields = ('title', 'description',
                  'url', 'thumbnail', 'published_date', 'language')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'location', 'birth_date')
