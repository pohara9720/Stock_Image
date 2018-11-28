from rest_framework import serializers
from .models import User,Image

class UserSerializer(serializers.ModelSerializer):
	images = serializers.StringRelatedField(many=True)
	class Meta: 
		model = User
		fields = ['id','name','email','password','images']

class ImageSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Image
		fields = ['id','created','stock_img','price','user']
