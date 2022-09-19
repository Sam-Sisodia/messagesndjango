
from django.contrib import admin
from django.urls import path
from appmessages import views

urlpatterns = [
    path('',views.RegisterView, name='register')
]