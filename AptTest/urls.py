from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from AptTest import views

app_name = 'AptTest'

urlpatterns = [

# path('interest/<int:pk>/', views.Questionform, name = 'question'),
path('apt-test/', views.apt_test, name = 'apt_test'),
path('apt-test/<int:pk>/result', views.apt_results, name = 'results'),



]

#TODO make quiz easy for new users. probably shouldn't include pk