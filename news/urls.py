from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import NewsViewSet, UserViewSet


router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
