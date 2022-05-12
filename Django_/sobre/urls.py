from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('mais_sobre', views.mais_sobre),
]
