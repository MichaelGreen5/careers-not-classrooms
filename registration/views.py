from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from registration.forms import SignUp, LoginForm, CustomPasswordResetForm, ProfileForm
from registration.models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth import login










class SignUp(CreateView):
    form_class = SignUp
    success_url = reverse_lazy('home')
    template_name = 'sign_up.html'

    def form_valid(self, form):
        request = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return request 
    
class CustomLogin(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')


class CreateProfileView(CreateView):
    template_name = 'profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()

        return super().form_valid(form)

#TODO profile to sort jobs by zone
class UpdateProfileView(UpdateView):
    model = Profile
    form_class =  ProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('AptTest:apt_test')

 

    



# class PasswordReset(PasswordResetView):
#     template_name = 'registration/reset_password.html'
#     form_class = CustomPasswordResetForm
    

# class PasswordResetSent(PasswordResetDoneView):
#     template_name = 'registration/password_reset_sent.html'
   

# class PasswordResetFormView(PasswordResetConfirmView):
#     template_name = 'registration/password_reset_form.html'

# class PasswordResetComplete(PasswordResetCompleteView):
#     template_name = 'registration/password_reset_done.html'