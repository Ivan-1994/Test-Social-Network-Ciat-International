from post.serializers import *
from post.models import *
from django.contrib.auth import authenticate
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import  APIView
from django.contrib.auth.models import User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostLikeSerializer

class PostUnLikeViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostUnLikeSerializer
