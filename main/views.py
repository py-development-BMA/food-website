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
import random
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

print(f"{bcolors.FAIL}\n[  VERSION  ]: 1.9.0 (created page for storage by ALEXEY)\n\n{bcolors.ENDC}")


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
				Subscribtion.objects.create(
					user=user,
					)
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
	subscriptions = Subscribtion.objects.get(user=request.user)
	context = {
	'test':123,
	'myrecipes':output_recipes,
	'subs':subscriptions,
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
		if form2.is_valid() and form2.cleaned_data.get('emailof_creator') == request.user.email:
			get_uuid = form2.cleaned_data.get('uuid_recipe')
			form2.save()
			myrecipe = RecipeProduct.objects.get(uuid_recipe=get_uuid)
			me_db_get = CustomUser.objects.get(email=request.user.email)
			me_db_get.my_recipes.add(myrecipe)
			me_db_get.amount_of_reciped += 1
			me_db_get.save()
			PostLike.objects.create(
				post=myrecipe,
			)
			nameProdField = form2.cleaned_data.get('name')
			return redirect('profile')
	context = {
	'form':form,
	}

	return render(request, 'main/addrecipe.html', context)

class patternRecipeView(DetailView):
	model = RecipeProduct
	template_name = 'main/patternrecipe.html'
	context_object_name = 'recipe'

class patternUserView(DetailView):
	model = CustomUser
	template_name = 'main/patternUser.html'
	context_object_name = 'user'
	def get_context_data(self, **kwargs):
		# В первую очередь получаем базовую реализацию контекста
		context = super(patternUserView, self).get_context_data(**kwargs)
		# Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
		print(self.object)
		is_followed = False
		for item in Subscribtion.objects.get(user=self.object).followed_by.all():
			if item.email == self.request.user.email:
				is_followed = True
				break
		context['subs'] = Subscribtion.objects.get(user=self.object)
		context['is_followed'] = is_followed
		context['userRecipes'] = reversed(CustomUser.objects.get(email=self.object.email).my_recipes.all())
		return context

	def post(self, request, pk):
		form = Subscribe()
		if request.method == 'POST':
			form = Subscribe(request.POST)
			if form.is_valid():
				emailToFollow = form.cleaned_data.get('emailToFollow')
				emailWhoFollows = form.cleaned_data.get('emailToFollow')

				toFollowUserCus = CustomUser.objects.get(email=emailToFollow)
				whoFollowsCus = CustomUser.objects.get(email=request.user)

				toFollowUser = Subscribtion.objects.get(user=toFollowUserCus)
				whoFollows = Subscribtion.objects.get(user=request.user)

				if form.cleaned_data.get('actionToDo') == 'subscribe':
					whoFollows.following.add(toFollowUserCus)
					toFollowUser.followed_by.add(whoFollowsCus)
				else:
					whoFollows.following.remove(toFollowUserCus)
					toFollowUser.followed_by.remove(whoFollowsCus)
				whoFollows.save()
				toFollowUser.save()
				return HttpResponse('ready')
			else:
				print(form)


def  mystorage(request):
  categories = ['Фрукти','Овочі','Молочні продукти','М\'ясні вироби','Морепродукти','Бакалія','Консерви та приправи','Напої','Заморожені продукти','Улюблені продукти']
  counter = [0,1,2,3,4,5,6,7,8,9]
  categories = zip(categories,counter)
  context = {
  'categories':categories,
  }

  return render(request, 'main/storage.html', context)





def feedPage(request):
	form = PostToLike()
	if request.method == 'POST':
		form = PostToLike(request.POST)
		if form.is_valid():
			post = PostLike.objects.get(post__uuid_recipe=form.cleaned_data.get('whatToLike'))
			user = Subscribtion.objects.get(user=request.user)
			if form.cleaned_data.get('actionToDoLike') == 'like':
				user.likedPosts.add(RecipeProduct.objects.get(uuid_recipe=form.cleaned_data.get('whatToLike')))
				post.usersLiked.add(request.user)

			else:
				user.likedPosts.remove(RecipeProduct.objects.get(uuid_recipe=form.cleaned_data.get('whatToLike')))
				post.usersLiked.remove(request.user)
			user.save()
			post.save()
			return HttpResponse('profile')
		else:
			print('error')
	else:
		users_subs = Subscribtion.objects.get(user=request.user)
		recipesToShow = []
		count = []
		user_sh = []
		is_liked = []
		k = 0
		for item in users_subs.following.all():
			if item.my_recipes.all().count() != 0:
				stop = 3
				for recipe in reversed(item.my_recipes.all()):
					if stop != 0:
						recipesToShow.append(recipe)
						count.append(k)
						user_sh.append(item)
						k+=1
						stop -=1
						if recipe in users_subs.likedPosts.all():
							is_liked.append(True)
						else:
							is_liked.append(False)

					else:
						break
		recipesZip = list(zip(recipesToShow, count, user_sh, is_liked))
		random.shuffle(recipesZip)
		context = {
			'recipesFeed':recipesZip,
		  }
		return render(request, 'main/feedpage.html', context)
