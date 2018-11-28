from django.shortcuts import render
from rest_framework import viewsets
from .models import User,Image
from .serializers import UserSerializer,ImageSerializer

# Create your views here
# This is where you put what happens when its a post get put patch etc

class UserView(viewsets.ModelViewSet):
	queryset= User.objects.all()
	serializer_class = UserSerializer

class ImageView(viewsets.ModelViewSet):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer