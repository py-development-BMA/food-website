from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
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
import itertools
from django.core import serializers
import json
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

print(f"{bcolors.FAIL}\n[  VERSION  ]: 2.1.0 (created page for storage by ALEXEY)\n\n{bcolors.ENDC}")


def signup(request):
	# usernames = ['qusert', 'morgenshtern', 'slavamarlow', 'olegSls', 'alex_sivak', 'btc_cook']
	# readNames = open('firstnames/us.txt', 'r', encoding='utf-8')
	# namesArr = readNames.read().split('\n')
	# readSurnames = open('surnames/us.txt', 'r', encoding='utf-8')
	# surnamesArr = readSurnames.read().split('\n')
	# for surname in surnamesArr:
	# 	nameRndm = random.choice(namesArr)
	# 	print('{1}_{0}@gmail.com'.format(nameRndm.lower(), surname.lower()))
	# 	print('{0}_{1}'.format(nameRndm.lower(), surname.lower()))
	# 	print(nameRndm)
	# 	print(surname)
	# 	print('-------------------------------------')
	# 	selecteduser = CustomUser.objects.create(
	# 			email='{1}_{0}@gmail.com'.format(nameRndm.lower(), surname.lower()),
	# 			username='{0}_{1}'.format(nameRndm.lower(), surname.lower()),
	# 			first_name=nameRndm,
	# 			last_name=surname,
	# 			password='Tornado2004',
	# 		)
	# 	Subscribtion.objects.create(
	# 			user=selecteduser,
	# 			)
	# first_names = []
	# last_names = []
	# k = 0
	# for username, first_name, last_name in zip(usernames, first_names, last_names):
	# 	k+=1
	# 	CustomUser.objects.create(
	# 		email='testemail{0}@gmail.com'.format(k),
	# 		username=username,
	# 		first_name=first_name,
	# 		last_name=last_name,
	# 		password='Tornado2004',
	# 	)
	# 	Subscribtion.objects.create(
	# 		user=user,
	# 		)
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


def emailexist(request):
	data = {'result':''}
	if request.method == 'GET':
		emailGet = request.GET.get('email')
		exists = CustomUser.objects.filter(email=emailGet).exists()
		if exists:
			data['result'] = 'exists'
		else:
			data['result'] = 'does not exist'
	return JsonResponse(data)



def homePage(request):
	return render(request, 'main/home.html')


def profile(request):
	users_recipes = CustomUser.objects.get(email=request.user.email)
	subscriptions = Subscribtion.objects.get(user=request.user)
	output_recipes = users_recipes.my_recipes.all()
	userPostsLikes = []
	for item in output_recipes:
		q_likesPost = PostLike.objects.get(post=item)
		userPostsLikes.append(q_likesPost)
	userPostsLikes.sort(key=lambda x: x.usersLiked.all().count(), reverse=True)
	#all_likedPosts = sorted(userPostsLikes, key=operator.attrgetter('usersLiked.count'))
	#for item in all_likedPosts:
	#	print(item.usersLiked.count())

	icons_interests = []
	names_interestst = []
	for item in request.user.interests.all():
		icons_interests.append(item.icon)
		names_interestst.append(item.name)
	for item in request.user.recipeDraft.all():
		print(item.name)
	k = 0
	quant = []
	for item in request.user.recipeDraft.all():
		quant.append(k)
		k += 1
	context = {
	'mydrafts':list(zip(request.user.recipeDraft.all(), quant)),
	'test':123,
	'myrecipes':output_recipes,
	'subs':subscriptions,
	'pop_recipes':itertools.islice(userPostsLikes, 5),
	'interests': itertools.islice(zip(icons_interests, names_interestst), 4)
	}
	return render(request, 'main/myaccount.html', context)


def removeDraft(request):
	if request.method == 'POST':
		if request.is_ajax():
			uuid_get = request.POST.get('uuid')
			user = CustomUser.objects.get(email=request.user.email)
			recipe = RecipeProduct.objects.get(uuid_recipe=uuid_get)
			user.recipeDraft.remove(recipe)
			user.save()
			recipe.delete()
		return HttpResponse('1')


def loadInterests(request):
	if request.method == 'GET':
		listOfInters = CustomUser.objects.get(email=request.GET.get('email')).interests.all()
		allInterests = AllInterests.objects.all().order_by('-peopleSelected')
		inside_arr = []
		my_interests = []
		arr_out = []
		for item in listOfInters:
			my_interests.append(item.name)

		for item in allInterests:
			print(item.name)
			inside_arr = []
			inside_arr.append(item.icon)
			inside_arr.append(item.english)
			inside_arr.append(item.name)
			if item.name in my_interests:
				inside_arr.append(1)
			else:
				inside_arr.append(0)
			arr_out.append(inside_arr)
		#print(arr_out)


		return HttpResponse(json.dumps(arr_out, ensure_ascii=False), content_type='application/json')
	if request.method == 'POST':
		form = InterestAction(request.POST)
		if form.is_valid():
			cuser = CustomUser.objects.get(email=request.user.email)
			interestSelected = AllInterests.objects.get(english=form.cleaned_data.get('newInterest'))
			if form.cleaned_data.get('actionToDo') == 'add':
				cuser.interests.add(interestSelected)
				interestSelected.peopleSelected += 1
				interestSelected.save()
				cuser.save()
			else:
				cuser.interests.remove(interestSelected)
				interestSelected.peopleSelected -= 1
				interestSelected.save()
				cuser.save()
		return HttpResponse('')




def loadSubs(request):
	if request.method == 'GET':
		if request.GET.get('wtd') == 'subs':
			qset = Subscribtion.objects.get(user__email=request.GET.get('email')).followed_by.all()
			mas = []
			startFrom = int(request.GET.get('start'))
			k = 35
			kn = 0
			print(startFrom)
			for item in qset:
				if kn >= startFrom:
					if k != 0:
						nmas = []
						nmas.append(item.pk)
						nmas.append(item.first_name)
						nmas.append(item.last_name)
						nmas.append(item.image_profile.url)
						nmas.append(item.username)
						mas.append(nmas)
						k-=1
					else:
						break
				else:
					kn+=1

			return HttpResponse(json.dumps(mas, ensure_ascii=False), content_type='application/json')
		if request.GET.get('wtd') == 'follows':
			qset = Subscribtion.objects.get(user__email=request.GET.get('email')).following.all()
			mas = []
			startFrom = request.GET.get('start')
			k = 35
			kn = 0
			print(startFrom)
			for item in reversed(qset):
				if kn >= int(startFrom):
					if k != 0:
						nmas = []
						nmas.append(item.pk)
						nmas.append(item.first_name)
						nmas.append(item.last_name)
						nmas.append(item.image_profile.url)
						nmas.append(item.username)
						mas.append(nmas)
						k-=1
					else:
						break
				else:
					kn+=1
			return HttpResponse(json.dumps(mas, ensure_ascii=False), content_type='application/json')
		#serialized_qs = serializers.serialize('json', qset)



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




def imageRecipeSave(request):
	if request.method == 'POST':
		form = imageRecipeS(request.POST, request.FILES)
		if request.is_ajax():
			image = request.FILES.get('image')
			uuid_get = request.POST.get('uuid_recipe')
			wtr = request.POST.get('wtr')
			print(wtr)
			myrecipe = RecipeProduct.objects.get(uuid_recipe=uuid_get)
			if wtr == 'mainImage':
				myrecipe.image_prod = image
			elif wtr == 'img1':
				myrecipe.image1 = image
			elif wtr == 'img2':
				myrecipe.image2 = image
			elif wtr == 'img3':
				myrecipe.image3 = image
			elif wtr == 'img4':
				myrecipe.image4 = image
			elif wtr == 'img5':
				myrecipe.image5 = image
			elif wtr == 'img6':
				myrecipe.image6 = image
			elif wtr == 'img7':
				myrecipe.image7 = image
			elif wtr == 'img8':
				myrecipe.image8 = image
			elif wtr == 'img9':
				myrecipe.image9 = image
			elif wtr == 'img10':
				myrecipe.image10 = image


			myrecipe.save()
	return HttpResponse('')



def newrecipe(request):
	user = request.user.username
	form = RecipeForm()

	if request.method == "POST":
		print(request.FILES)
		print(request.POST)
		form2 = RecipeAjaxForm(request.POST, request.FILES)
		if form2.is_valid() and form2.cleaned_data.get('emailof_creator') == request.user.email:
			print(1)
			if RecipeProduct.objects.filter(uuid_recipe=form2.cleaned_data.get('uuid_recipe')).count() == 0:
				if form2.cleaned_data.get('actionToDo') == 'name':
					RecipeProduct.objects.create(
						uuid_recipe=form2.cleaned_data.get('uuid_recipe'),
						name=form2.cleaned_data.get('value'),
						adderOf=request.user.email,
					)
					get_uuid = form2.cleaned_data.get('uuid_recipe')
					myrecipe = RecipeProduct.objects.get(uuid_recipe=get_uuid)
					me_db_get = CustomUser.objects.get(email=request.user.email)
					me_db_get.recipeDraft.add(myrecipe)
					me_db_get.save()
					return HttpResponse('')
			else:
				print(form2.cleaned_data.get('value'))
				get_uuid = form2.cleaned_data.get('uuid_recipe')
				myrecipe = RecipeProduct.objects.get(uuid_recipe=get_uuid)
				if form2.cleaned_data.get('actionToDo') == 'name':
					myrecipe.name = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'submitForm':
					me = CustomUser.objects.get(email=request.user.email)
					me.recipeDraft.remove(myrecipe)
					myrecipe.active = True
					me.save()
				elif form2.cleaned_data.get('actionToDo') == 'description':
					myrecipe.description = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'time':
					myrecipe.time = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'category':
					myrecipe.category = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'hardnessCook':
					myrecipe.hardnessCook = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc1':
					myrecipe.desc1 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc2':
					myrecipe.desc2 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc3':
					myrecipe.desc3 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc4':
					myrecipe.desc4 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc5':
					myrecipe.desc5 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc6':
					myrecipe.desc6 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc7':
					myrecipe.desc7 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc8':
					myrecipe.desc8 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc9':
					myrecipe.desc9 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == 'desc10':
					myrecipe.desc10 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas1'):
					myrecipe.ingredient1 = form2.cleaned_data.get('ingredient')
					myrecipe.mas1 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas2'):
					myrecipe.ingredient2 = form2.cleaned_data.get('ingredient')
					myrecipe.mas2 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas3'):
					myrecipe.ingredient3 = form2.cleaned_data.get('ingredient')
					myrecipe.mas3 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas4'):
					myrecipe.ingredient4 = form2.cleaned_data.get('ingredient')
					myrecipe.mas4 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas5'):
					myrecipe.ingredient5 = form2.cleaned_data.get('ingredient')
					myrecipe.mas5 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas6'):
					myrecipe.ingredient6 = form2.cleaned_data.get('ingredient')
					myrecipe.mas6 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas7'):
					myrecipe.ingredient7 = form2.cleaned_data.get('ingredient')
					myrecipe.mas7 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas8'):
					myrecipe.ingredient8 = form2.cleaned_data.get('ingredient')
					myrecipe.mas8 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas9'):
					myrecipe.ingredient9 = form2.cleaned_data.get('ingredient')
					myrecipe.mas9 = form2.cleaned_data.get('value')
				elif form2.cleaned_data.get('actionToDo') == ('mas10'):
					myrecipe.ingredient10 = form2.cleaned_data.get('ingredient')
					myrecipe.mas10 = form2.cleaned_data.get('value')
				#get_uuid = form2.cleaned_data.get('uuid_recipe')
				myrecipe.save()
				#myrecipe = RecipeProduct.objects.get(uuid_recipe=get_uuid)
				#me_db_get = CustomUser.objects.get(email=request.user.email)
				#me_db_get.my_recipes.add(myrecipe)
				#me_db_get.recipeDraft = myrecipe
				#me_db_get.amount_of_reciped += 1
				#me_db_get.save()
				#PostLike.objects.create(
				#	post=myrecipe,
				#)
				#nameProdField = form2.cleaned_data.get('name')
				#return HttpResponse('')
	context = {
	'form':form,
	}

	return render(request, 'main/addrecipe.html', context)

class patternRecipeView(DetailView):
	model = RecipeProduct
	template_name = 'main/patternrecipe.html'
	context_object_name = 'recipe'



class editdraft(DetailView):
	model = RecipeProduct
	template_name = 'main/editDraftPattern.html'
	context_object_name = 'recipe'
	def get_context_data(self, **kwargs):
		context = super(editdraft, self).get_context_data(**kwargs)
		print(self.object.ingredient1)
		k = 2
		ks = []
		ingrs_arr = []
		mas_arr = []
		descs_arr = []
		descs_plone_arr = []
		img_urls_arr = []
		img_urls_plone = []
		k2 = 1
		k2_arr = []
		while k != 11:
			ks.append(k)
			exec("ingrs_arr.append(self.object.ingredient{})".format(k))
			exec("mas_arr.append(self.object.mas{})".format(k))
			exec("descs_arr.append(self.object.desc{})".format(k))
			exec("img_urls_arr.append(self.object.image{}.url)".format(k))
			if k != 10:
				exec("img_urls_plone.append(self.object.image{}.url)".format(k+1))
				exec("descs_plone_arr.append(self.object.desc{})".format(k+1))
			else:
				img_urls_plone.append(1)
				descs_plone_arr.append(1)
			k+=1
		while k2 != 11:
			k2_arr.append(k2)
			k2 += 1
		print(ks)
		print(ingrs_arr)
		context['allIngrs'] = list(zip(ingrs_arr, mas_arr, ks))
		context['allSteps'] = list(zip(descs_arr, img_urls_arr, img_urls_plone, descs_plone_arr, ks))
		context['k_arr'] = k2_arr
		return context




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
		output_recipes = CustomUser.objects.get(email=self.object.email).my_recipes.all()
		userPostsLikes = []
		for item in output_recipes:
			q_likesPost = PostLike.objects.get(post=item)
			userPostsLikes.append(q_likesPost)
		userPostsLikes.sort(key=lambda x: x.usersLiked.all().count(), reverse=True)
		icons_interests = []
		names_interestst = []
		for item in self.object.interests.all():
			icons_interests.append(item.icon)
			names_interestst.append(item.name)
		context['pop_recipes'] = itertools.islice(userPostsLikes, 5)
		context['subs'] = Subscribtion.objects.get(user=self.object)
		context['is_followed'] = is_followed
		context['interests'] = itertools.islice(zip(icons_interests, names_interestst), 4)
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
		likesCount = []
		comment = []
		postsAmount = 1
		all_recipesPk = []
		for item in users_subs.following.all():

				if item.my_recipes.all().count() != 0:
					stop = 3
					for recipe in reversed(item.my_recipes.all()):
						all_recipesPk.append(recipe.pk)
		print(all_recipesPk)
		for i in range(3):
			rnum = int(random.choice(all_recipesPk))
			postlike = PostLike.objects.get(post=RecipeProduct.objects.get(pk=rnum))
			likesCount.append(postlike.usersLiked.all().count())
			recipesToShow.append(postlike.post)
			count.append(i)
			user_sh.append(CustomUser.objects.get(email=postlike.post.emailof_creator))
			all_recipesPk.remove(rnum)
			if postlike.post in users_subs.likedPosts.all():
				is_liked.append(True)
			else:
				is_liked.append(False)
			print(all_recipesPk)




		recipesZip = list(zip(recipesToShow, count, user_sh, is_liked, likesCount))
		random.shuffle(recipesZip)
		context = {
			'recipesFeed':recipesZip,
			'all_recipesPk':all_recipesPk,
		  }
		return render(request, 'main/feedpage.html', context)


def openComments(request):
	if request.method == 'GET':
		all_comments = Comment.objects.filter(recipe__uuid_recipe=request.GET.get('post'))
		commReturn = []
		for item in all_comments:
			x2arr = []
			x2arr.append(item.user.image_profile.url)
			x2arr.append(item.user.first_name + ' ' + item.user.last_name)
			x2arr.append(item.user.rank)
			x2arr.append(item.text)
			x2arr.append(item.pk)
			commReturn.append(x2arr)
		out = 1

		commReturn.reverse()
		return HttpResponse(json.dumps(commReturn, ensure_ascii=False), content_type='application/json')

def saveComment(request):
	if request.method == 'POST':
		print(request.POST.get('text'))
		Comment.objects.create(
		user=request.user,
		text=request.POST.get('text'),
		recipe=RecipeProduct.objects.get(uuid_recipe=request.POST.get('recipe_uuid'))
		)
		out = 1
		return HttpResponse(json.dumps(out, ensure_ascii=False), content_type='application/json')


def friendrec(request):
	data = {}
	usersRec = []
	conc_count = []
	out_Recs = []
	myInterests = request.user.interests.all()
	if request.method == 'GET':
		userSubs = Subscribtion.objects.get(user=request.user)
		k = 4
		for user_fol in userSubs.following.all():
			if k != 0:
				userExFolowers = Subscribtion.objects.get(user=user_fol).following.all()
				for item in userExFolowers:
					print(item.email)
					if item.my_recipes.all().count() >= 5:
						if item.email != request.user.email and item not in usersRec and item not in userSubs.following.all():
							sp = 0
							if len(myInterests)>=len(item.interests.all()):
								for inter in myInterests:
									if inter in item.interests.all():
										sp += 1
								if sp >= 3:
									usersRec.append(item)
									conc_count.append(sp)
							else:
								for inter in item.interests.all():
									if inter in myInterests:
										sp += 1
								if sp >= 3:
									usersRec.append(item)
									conc_count.append(sp)

	out_Recs = list(zip(usersRec, conc_count))
	out_Recs = reversed(sorted(out_Recs, key = lambda x: x[1]))
	a = []
	out = []
	k1 = 0
	print(out_Recs)
	for user, conc in out_Recs:
		if k1 != 4:
			a = []
			a.append(user.image_profile.url)
			a.append(user.first_name)
			a.append(user.last_name)
			a.append(user.rank)
			a.append(conc)
			a.append(user.pk)
			k += 1
			out.append(a)
		else:
			break
	return HttpResponse(json.dumps(out, ensure_ascii=False), content_type='application/json')



def getRecipes(request):
	if request.method == 'GET':
		posts = []
		post = []
		users_subs = Subscribtion.objects.get(user=request.user)
		recipesToShow = []
		count = []
		user_sh = []
		is_liked = []
		k = int(request.GET.get('data'))
		likesCount = []
		comment = []
		all_recipesPk = request.GET.getlist('notloaded[]')
		for i in range(3):
			rnum = int(random.choice(all_recipesPk))

			recipe = RecipeProduct.objects.get(pk=rnum)
			postlike = PostLike.objects.get(post=recipe)
			item = CustomUser.objects.get(email=recipe.emailof_creator)

			post = []
			post.append(item.pk)
			post.append('{0} {1}'.format(item.first_name, item.last_name)) # USERS NAME + SURNAME
			post.append(item.rank)
			post.append(item.image_profile.url)
			post.append(recipe.description)
			post.append(recipe.image_prod.url)
			post.append(postlike.usersLiked.all().count())
			post.append(k)
			k+=1
			if recipe in users_subs.likedPosts.all():
				post.append(1)
			else:
				post.append(0)
			post.append(item.email)
			post.append(recipe.uuid_recipe)
			post.append(recipe.pk)
			all_recipesPk.remove(str(rnum))
			posts.append(post)



		ret_arr = []
		ret_arr.append(posts)
		ret_arr.append(all_recipesPk)
		return HttpResponse(json.dumps(ret_arr, ensure_ascii=False), content_type='application/json')

def  mystorage(request):
	categories = ['Фрукти','Овочі','Молочні продукти','М\'ясні вироби','Морепродукти','Бакалія','Консерви та приправи','Напої','Заморожені продукти','Улюблені продукти']

	categories_names = categories
	counter = [0,1,2,3,4,5,6,7,8,9]
	categories = zip(categories,counter)
	list0 = []


	if request.method == 'POST':
		form = AddProduct(request.POST)
		if form.is_valid():
			for item in AllProduct.objects.all():
				list0.append(item.nameUa)
			if form.cleaned_data.get('nameUa') in list0:
				if not UserProductQuantity.objects.filter(nameUa=AllProduct.objects.get(nameUa=form.cleaned_data.get('nameUa')) ,user = CustomUser.objects.get(email=request.user.email).id).exists():
					UserProductQuantity.objects.create(
						user=request.user,
						nameUa=AllProduct.objects.get(nameUa=form.cleaned_data.get('nameUa')),
						quantity=form.cleaned_data.get('quantity')
					)
					CustomUser.objects.get(email=request.user.email).my_products.add(AllProduct.objects.get(nameUa=form.cleaned_data.get('nameUa')))
					return HttpResponse(json.dumps(1, ensure_ascii=False), content_type='application/json')
			else:
				return HttpResponse(json.dumps(0, ensure_ascii=False), content_type='application/json')


	else:
		q_array = []

		all_products = CustomUser.objects.get(email=request.user.email).my_products.all()
		for item in all_products:
			k = UserProductQuantity.objects.get(user=request.user, nameUa=item).quantity
			q_array.append(k)

		products = list(zip(all_products,q_array))

		context = {
		'categories':categories,
		'categories_names':categories_names,
		'all_products':all_products,
		'products_array' : products,
		}
		return render(request, 'main/storage.html', context)

def alexPost(request):
	if request.method == 'POST':
		form = AlexEx(request.POST)
		if form.is_valid():
			ExampleAlex.objects.create(
				user2=request.user,
				my_products=form.cleaned_data.get('alexExText'),
				quantity1=form.cleaned_data.get('quantity1')
			)
	return render(request, 'main/alexPost.html')




def showresults(request):
	if request.method == 'GET':
		matched1 = []
		categories = ['Фрукти','Овочі','Молочні продукти','М\'ясо','Риба','Бакалія','Консерви та приправи','Напої','Заморожені продукти','Улюблені продукти']
		fav_p = CustomUser.objects.get(email=request.user.email).favorites.all()
		for item in AllProduct.objects.all():
			mn = []
			mn.append(item.nameUa)
			mn.append(categories.index(item.category))
			mn.append(item.pk)
			if fav_p.filter(pk=item.pk).count() != 0:
				mn.append(1)
			else:
				mn.append(0)
			matched1.append(mn)
		#print(matched1)
		return HttpResponse(json.dumps(matched1, ensure_ascii=False), content_type='application/json')


def recipeConstructor(request):
	recipes = RecipeProduct.objects.all()
	k = []
	products = ["Картопля", "Курка", "Помідори", "Часник", "Цибуля", "Оцет", "Яйця", "Свинина", "Паста", "Кетчуп"]
	for i in range(recipes.count()):
		k.append(i)
	context = {
		'recipes':list(zip(recipes, k)),
		'products':products,
		'ln':recipes.count(),
	}
	return render(request, 'main/recipeConstructor.html', context)

def rewards(request):
	achievements = Achievements.objects.all()
	numbs = []
	for i in range(achievements.count()):
		numbs.append(i)
	rewards = zip(numbs, achievements)
	context = {
		'rewards':rewards,
		'ln':achievements.count(),
	}
	return render(request, 'main/rewards.html', context)





def addfav(request):
	if request.method == 'POST':
		user = CustomUser.objects.get(email=request.user.email)
		if request.POST.get("wtd") == "add":
			user.favorites.add(AllProduct.objects.get(nameUa = request.POST.get("name")))
		else:
			user.favorites.remove(AllProduct.objects.get(nameUa = request.POST.get("name")))
		user.save()
	return HttpResponse("1")






def alexPost(request):
	if request.method == 'POST':
		form = AlexEx(request.POST)
		if form.is_valid():
			ExampleAlex.objects.create(
				user2=request.user,
				my_products=form.cleaned_data.get('alexExText')
			)
	return render(request, 'main/alexPost.html')
