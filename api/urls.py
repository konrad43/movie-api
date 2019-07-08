from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movies')
router.register(r'comments', views.CommentViewSet, basename='comments')
router.register(r'top', views.TopViewSet, basename='top')

urlpatterns = [
    path('', include(router.urls))
]
