from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import ArticleViewSet, AuthenticationView, GamerfetaminaViewSet, HelloView, UserView

urlpatterns = [
    path('articles/', ArticleViewSet.as_view()),
    path('articles/gamerfetamina/', GamerfetaminaViewSet.as_view()),

    path('hello/', HelloView.as_view(), name='hello'),
    path('token/', AuthenticationView.as_view(), name='token'),
    path('profile/', UserView.as_view(), name='profile'),
    path('profile/<str:username>/', UserView.as_view(), name='profile'),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
