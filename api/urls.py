from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api', views.ArticleViewSet, base_name="articles")
urlpatterns = router.urls
