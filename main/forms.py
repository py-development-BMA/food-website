from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, PasswordInput, EmailInput
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