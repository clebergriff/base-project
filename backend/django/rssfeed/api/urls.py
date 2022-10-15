from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import ArticleViewSet, GamerfetaminaViewSet

urlpatterns = [
    path('articles/', ArticleViewSet.as_view()),
    path('articles/gamerfetamina/', GamerfetaminaViewSet.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
