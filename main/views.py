from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
#from .forms import *
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
	return render(request, 'main/sign_up.html')