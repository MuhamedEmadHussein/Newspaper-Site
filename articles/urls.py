from django.urls import path
from .views import (
                 ArticleListView,
                 ArticleDetailView,
                 ArticleUpdateView,
                 ArticleDeleteView,
                 ArticleCreateView)

urlpatterns = [
    path("<int:pk>/",view=ArticleDetailView.as_view(),name='article_detail'),   
    path("<int:pk>/edit/",view=ArticleUpdateView.as_view(),name='article_edit'),   
    path("<int:pk>/delete/",view=ArticleDeleteView.as_view(),name='article_delete'),  
    path("new/",view=ArticleCreateView.as_view(),name='article_new'),   
    path("",view=ArticleListView.as_view(),name='article_list'),   
]