from rest_framework import viewsets
from .serializers import PostSerializer,UserSerializer

from hacker.models import NewsObject 
from django.contrib.auth import get_user_model

# Create your views here.
class PostViewset(viewsets.ModelViewSet):
    queryset = NewsObject.entire.all()
    serializer_class = PostSerializer

# class UserViewset(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer