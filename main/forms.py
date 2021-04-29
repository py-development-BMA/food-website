from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, PasswordInput, EmailInput, ImageField
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ("email", 'access_to_data')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		del self.fields['password2']



class CustomUserEdit(ModelForm):
	class Meta:
		model = CustomUser
		fields = "__all__"
		exclude = ['my_recipes','email', 'amount_of_reciped', 'achievements', 'purchases', 'sex', 'date_joined', 'date_of_birth', 'ip_adress', 'rank', 'rank_percentage', 'access_to_data', 'is_user', 'is_staff', 'is_superuser', 'last_login', 'password', 'recipeDraft', 'my_recipes', 'interests']




class RecipeForm(ModelForm):
	class Meta:
		model = RecipeProduct
		fields = '__all__'
		widgets = {
		'name':TextInput(attrs={
			'class': "nameAdd",
			'placeholder':"Назва страви"
			}),
		'time':TextInput(attrs={
			'class': "timeAdd",
			'placeholder':"Час для приготування"
			}),
		'description':TextInput(attrs={
			'class': "descriptionAdd",
			'placeholder':"Короткий опис"
			}),
		}

class RecipeAjaxForm(forms.Form):
	actionToDo = forms.CharField(max_length=200, required=False)
	ingredient = forms.CharField(max_length=200, required=False)
	value = forms.CharField(max_length=1000, required=False)
	emailof_creator = forms.CharField(max_length=100, required=False)
	uuid_recipe = forms.CharField(max_length=100, required=True)


class Subscribe(forms.Form):
	actionToDo = forms.CharField(max_length=100)
	emailToFollow = forms.CharField(max_length=100)
	emailWhoFollows = forms.CharField(max_length=100)


class PostToLike(forms.Form):
	actionToDoLike = forms.CharField(max_length=30)
	whoLikes = forms.CharField(max_length=100)
	whatToLike = forms.CharField(max_length=100)

class InterestAction(forms.Form):
	actionToDo = forms.CharField(max_length=100, required=False)
	newInterest = forms.CharField(max_length=100, required=False)


class imageRecipeS(forms.Form):
	file = forms.FileField()

class AlexEx(forms.Form):
	alexExText = forms.CharField(max_length=300, required=False)
