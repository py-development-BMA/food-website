from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


class MyAccountManager(BaseUserManager):
	def create_user(self, email, password, access_to_data):
		user = self.model(
			email=self.normalize_email(email),
			access_to_data=True,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user
	def create_superuser(self, email, password, access_to_data):
		user = self.create_user(
			email,
			password=password,
			access_to_data=True,
			)
		user.is_staff = True
		user.access_to_data = True
		user.is_active = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class CustomUser(AbstractBaseUser):
	first_name = models.CharField("first_name", max_length=50, blank=True)
	last_name = models.CharField("last_name", max_length=50, blank=True)
	email = models.CharField("email", max_length=250, unique=True)
	about = models.TextField('about', blank=True)
	SEX = (('Чоловіча','male'),('Жіноча','female'))
	sex = models.CharField('Стать', max_length=200, null=True, choices=SEX, blank=True)
	date_joined = models.DateTimeField('date_creat',auto_now_add=True, null=True)
	ip_adress = models.CharField('ip_user', max_length=200, null=True, blank=True)
	access_to_data = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['access_to_data', 'password']
	objects = MyAccountManager()
	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True