from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from AptTest import views

app_name = 'AptTest'

urlpatterns = [

path('apt-test-pre/', views.first_questions, name = 'first_questions'), 
path('apt-test/', views.apt_test, name = 'apt_test'),

path('apt-test/<int:pk>/result', views.apt_results, name = 'results'),



]

#TODO make quiz easy for new users. probably shouldn't include pk