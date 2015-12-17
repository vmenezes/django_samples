from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from app import forms


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('welcome')
        return render(request, 'app/home.html')
	
	
class WelcomeView(View):
    def get(self, request):
        return render(request, 'app/welcome.html')
    
    
class CreateUser(View):
    def post(self, request):
        if request.user.is_authenticated():
            return redirect('welcome')
        frm_username = request.POST['username']
        frm_email = request.POST['email']
        frm_password = request.POST['password']
        user = User.objects.create_user(frm_username, frm_email, frm_password)
        if user:
            user = authenticate(username=frm_username, password=frm_password)
            login(request, user)
            return redirect('welcome')
        return redirect('auth:login')