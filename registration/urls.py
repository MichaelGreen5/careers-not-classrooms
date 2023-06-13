
from django.urls import path
from registration import views

from django.contrib.auth import views as auth_views
from django.conf import settings

app_name = 'reg'

urlpatterns = [

path('signup/', views.SignUp.as_view(), name = 'signup'),
path("logout/", auth_views.LogoutView.as_view(), name= 'logout'),
path("login/", views.CustomLogin.as_view(), name = 'login'),
path('profile/', views.CreateProfileView.as_view(), name = 'profile'),
path('profile/update/<int:pk>/', views.UpdateProfileView.as_view(), name = 'update_profile'),

]