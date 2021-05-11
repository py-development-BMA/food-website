from django.urls import path

from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
	path('signup/', views.signup, name="signup"),
	path('profile/', views.profile, name="profile"),
	path('edit_profile/', views.edit_profile, name="edit_profile"),
	path('', views.homePage, name="home"),
	path('login/', views.login_page, name="login_page"),
	path('logout/', views.logout_page, name="logout_page"),
	path('newrecipe/', views.newrecipe, name="newrecipe"),
	path('mystorage/', views.mystorage, name="mystorage"),
	path('<int:pk>/viewrecipe', views.patternRecipeView.as_view(), name="viewrecipe"),
	path('<int:pk>/viewuser', views.patternUserView.as_view(), name="viewuser"),
	path('<int:pk>/editdraft', views.editdraft.as_view(), name="editdraft"),
	path('feed/', views.feedPage, name="feed"),
	path('alexPost/', views.alexPost, name="alexPost"),
	path('emailexist/', views.emailexist, name="emailexist"),
	path('loadsubs/', views.loadSubs, name="loadSubs"),
	path('friendrec/', views.friendrec, name="friendrec"),
	path('loadInterests/', views.loadInterests, name="loadInterests"),
	path('imageRecipeSave/', views.imageRecipeSave, name="imageRecipeSave"),
	path('removeDraft/', views.removeDraft, name="removeDraft"),
	path('openComments/', views.openComments, name="openComments"),
	path('saveComment/', views.saveComment, name="saveComment"),
	path('getRecipes/', views.getRecipes, name="getRecipes"),
	path('showresults/', views.showresults, name="showresults"),
	path('addfav/', views.addfav, name="addfav"),
	path('recipeConstructor/', views.recipeConstructor, name="recipeConstructor"),
	path('rewards/', views.rewards, name="rewards"),

]
