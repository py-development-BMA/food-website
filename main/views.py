from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from django.core.mail import send_mail
import re
#from .tasks import *



def signup(request):
	if 1==1:
		print(1) 
		form = CustomUserCreationForm()
		context = {'form': form}

		if request.method == "POST":
			print("got")
			form = CustomUserCreationForm(request.POST)
			print(request.POST)
			if form.is_valid():
				user = form.save()
				print("SAVED!")
				return redirect('home')
				#username = form.cleaned_data.get('username')
				#email = form.cleaned_data.get('email')
		return render(request, 'main/sign_up.html', context)


def homePage(request):
	return render(request, 'main/home.html')


def profile(request):
	context = {
	'test':123,
	}
	return render(request, 'main/myaccount.html', context)


def edit_profile(request):
	form = CustomUserEdit()
	if request.method == "POST":
		form = CustomUserEdit(request.POST)
		user_info = CustomUser.objects.get(email=request.user)
		print(user_info.email)
		print(request.POST)
		if form.is_valid():
			user_info.first_name = form.cleaned_data.get('first_name')
			user_info.last_name  = form.cleaned_data.get('last_name')
			user_info.about = form.cleaned_data.get('about')
			user_info.username = form.cleaned_data.get('username')
			user_info.save()
			return redirect('profile')

	context = {
	'test':123,
	'form':form,
	}
	return render(request, 'main/edit_account.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else: 
        error = ''
        if request.method == "POST":
            username = request.POST.get('email')
            password = request.POST.get("password1")
            user = authenticate(request, email=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                error = "Не верное имя пользователя или пароль"
                context = {'error':error}
                return render(request, 'main/login.html', context)
        context = {'error':error}
        return render(request, 'main/login.html')

def logout_page(request):
	logout(request)
	return redirect('login_page')


