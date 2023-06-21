from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from AptTest import views

app_name = 'AptTest'

urlpatterns = [

path('question/<int:pk>/', views.first_question_view, name = 'first_question'), 
path('interests/<int:pk>/', views.questions, name = 'question'),
path('start/', views.start_quiz, name= 'start_quiz'),
path('apt-test/<int:pk>/result', views.apt_results, name = 'results'),



]
