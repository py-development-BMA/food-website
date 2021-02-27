from django.urls import path

from django.contrib.auth import views as auth_views 
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
	path('signup/', views.signup, name="signup"),
	path('', views.homePage, name="home"),
]