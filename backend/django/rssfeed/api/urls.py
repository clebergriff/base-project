from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import ArticleViewSet, AuthenticationView, GamerfetaminaViewSet, HelloView, ImageUploadView, UserView

urlpatterns = [
    path('articles/', ArticleViewSet.as_view()),
    path('articles/gamerfetamina/', GamerfetaminaViewSet.as_view()),

    path('hello/', HelloView.as_view(), name='hello'),
    path('token/', AuthenticationView.as_view(), name='token'),
    path('profile/', UserView.as_view(), name='profile'),
    path('profile/<str:username>/', UserView.as_view(), name='profile'),
    path('image/', ImageUploadView.as_view(), name='image'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
