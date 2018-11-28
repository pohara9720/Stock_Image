from django.urls import path,include
from .views import UserView,ImageView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserView,base_name='User')
router.register('images',ImageView,base_name='Image')

urlpatterns = [
    path('',include(router.urls))
]

