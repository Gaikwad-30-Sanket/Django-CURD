from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.index),  #the path for our index view
]