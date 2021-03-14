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
		exclude = ['email', 'amount_of_reciped', 'achievements', 'purchases', 'sex', 'date_joined', 'date_of_birth', 'ip_adress', 'rank', 'rank_percentage', 'access_to_data', 'is_user', 'is_staff', 'is_superuser', 'last_login', 'password']




class RecipeForm(ModelForm):
	class Meta:
		model = RecipeProduct
		fields = '__all__'
		widgets = {
		'name':TextInput(attrs={
			'class': "nameAdd",
			'placeholder':"Название блюда"
			}),
		'time':TextInput(attrs={
			'class': "timeAdd",
			'placeholder':"Длительность приготовления"
			}),
		'description':TextInput(attrs={
			'class': "descriptionAdd",
			'placeholder':"Короткое описание(5-15 слов)"
			}),
		}