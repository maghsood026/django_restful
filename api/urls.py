from django.urls import path
from . import views


urlpatterns = [
    path('get/', views.ArticleViewToGet.as_view(), name="show article"),
    path('get/<pk>', views.ArticleDetailView.as_view(), name="show detail of article"),
    path('post/', views.ArticleViewToPost.as_view(), name="post new article"),
    path('update/<pk>', views.ArticleViewToUpdate.as_view(), name="update article"),
    path('delete/<pk>', views.ArticleViewToDelete.as_view(), name="delete article")
]
