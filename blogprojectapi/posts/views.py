from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Post 
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer,UserSerializer
from django.contrib.auth import get_user_model


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer