from django.db import models

# Create your models here.
# After models are set run 
#python manage.py makemigrations 
#python manage.py migrate

class User(models.Model):
	name = models.CharField(max_length=50)
	email= models.CharField(max_length=50)
	password = models.CharField(max_length=150)

class Image(models.Model):
	created = models.DateTimeField()
	stock_img = models.CharField(max_length=200)
	user = models.ForeignKey(User, related_name='images',on_delete=models.CASCADE) 
	price= models.PositiveIntegerField()