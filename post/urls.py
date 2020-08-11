from post.views import *
from django.urls import path

urlpatterns = [
    path("create/", PostViewSet.as_view({'get': 'list', 'post': 'create'}), name="post_create"),
    path("like/<int:pk>", PostLikeViewSet.as_view({'put': 'update'}), name="post_like"),
    path("unlike/<int:pk>", PostUnLikeViewSet.as_view({'put': 'update'}), name="post_unlike"),

]
