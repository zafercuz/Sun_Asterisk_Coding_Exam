from django.urls import path

from article.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    vote

urlpatterns = [
    path('', ArticleListView.as_view(), name="article_home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),
    path('article/create', ArticleCreateView.as_view(), name="article_create"),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name="article_update"),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name="article_delete"),

    path('article/vote', vote, name="article_vote"),
]
