from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.testing , name="testing"),
    path('mail', views.mail , name="mail"),


]

