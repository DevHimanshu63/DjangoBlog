from django.contrib import admin
from django.urls import path,include
from blogApp import views

urlpatterns = [
    path('',views.bloghome ,name='bloghome'),
     path('<str:slug>',views.blogpost ,name='blogpost'),


]