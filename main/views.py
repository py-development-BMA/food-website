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

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.FAIL}\n[  VERSION  ]: 1.8.2 (created page for adding recipe)\n\n{bcolors.ENDC}")


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
	users_recipes = CustomUser.objects.get(email=request.user.email)
	output_recipes = users_recipes.my_recipes.all()
	context = {
	'test':123,
	'myrecipes':output_recipes,
	}
	return render(request, 'main/myaccount.html', context)


def edit_profile(request):
	user = request.user
	form = CustomUserEdit(instance=user)
	if request.method == "POST":
		form = CustomUserEdit(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
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


def newrecipe(request):
	user = request.user.username
	form = RecipeForm()

	if request.method == "POST":
		form2 = RecipeForm(request.POST, request.FILES)
		if form2.is_valid():
			get_uuid = form2.cleaned_data.get('uuid_recipe')
			form2.save()
			myrecipe = RecipeProduct.objects.get(uuid_recipe=get_uuid)
			me_db_get = CustomUser.objects.get(email=request.user.email)
			me_db_get.my_recipes.add(myrecipe)
			me_db_get.amount_of_reciped += 1
			me_db_get.save()
			nameProdField = form2.cleaned_data.get('name')
			return redirect('profile')
	context = {
	'form':form,
	}

	return render(request, 'main/addrecipe.html', context)

def  mystorage(request):

	context = {
	'form':1,
	}

	return render(request, 'main/storage.html', context)