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


class Achievements(models.Model):
	fast_start = models.BooleanField(default=False)
	#here to put names of achiements they are already connected to CustomUser


class CustomUser(AbstractBaseUser):
	first_name = models.CharField("first_name", max_length=50, blank=True)
	last_name = models.CharField("last_name", max_length=50, blank=True)
	email = models.CharField("email", max_length=250, unique=True)
	about = models.TextField('about', blank=True)
	SEX = (('Чоловіча','male'),('Жіноча','female'))
	username = models.CharField("username", max_length=50, unique=True, blank=True)
	achievements = models.ManyToManyField(Achievements)
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


class RecipeProduct(models.Model):
	creator = models.OneToOneField(CustomUser, null=True, on_delete=models.PROTECT)
	CATEGORY = (
		('Горячие блюда','Горячие блюда'), ('Бульоны и супы','Бульоны и супы'), ('Салаты','Салаты'), ('Закуски','Закуски'), ('Выпечка','Выпечка'), ('Десерты','Десерты'), ('Соусы','Соусы'))
	HARDNESS = (
		('Очень легко', 'Очень легко'),('Легко','Легко'),('Средняя сложность','Средняя сложность'),('Нужен опыт','Нужен опыт'),('Сложно','Сложно'),('Очень сложно','Очень сложно'))	
	name = models.CharField('name', max_length=250, null=True)
	time = models.CharField('time', max_length=50, null=True)
	adderOf = models.CharField("adderOf", max_length=100, null=True)
	category = models.CharField('category', max_length=200, null=True, choices=CATEGORY)
	hardnessCook = models.CharField('hardness', max_length=200, null=True, choices=HARDNESS)
	ingredient1 = models.CharField('ingredients1', null=True, blank=True, max_length=200)
	ingredient2 = models.CharField('ingredients2', null=True, blank=True, max_length=200)
	ingredient3 = models.CharField('ingredients3', null=True, blank=True, max_length=200)
	ingredient4 = models.CharField('ingredients4', null=True, blank=True, max_length=200)
	ingredient5 = models.CharField('ingredients5', null=True, blank=True, max_length=200)
	ingredient6 = models.CharField('ingredients6', null=True, blank=True, max_length=200)
	ingredient7 = models.CharField('ingredients7', null=True, blank=True, max_length=200)
	ingredient8 = models.CharField('ingredients8', null=True, blank=True, max_length=200)
	ingredient9 = models.CharField('ingredients9', null=True, blank=True, max_length=200)
	ingredient10 = models.CharField('ingredients10', null=True, blank=True, max_length=200)
	mas1 = models.CharField("mas1", null=True, blank=True, max_length=100)
	mas2 = models.CharField("mas2", null=True, blank=True, max_length=100)
	mas3 = models.CharField("mas3", null=True, blank=True, max_length=100)
	mas4 = models.CharField("mas4", null=True, blank=True, max_length=100)
	mas5 = models.CharField("mas5", null=True, blank=True, max_length=100)
	mas6 = models.CharField("mas6", null=True, blank=True, max_length=100)
	mas7 = models.CharField("mas7", null=True, blank=True, max_length=100)
	mas8 = models.CharField("mas8", null=True, blank=True, max_length=100)
	mas9 = models.CharField("mas9", null=True, blank=True, max_length=100)
	mas10 = models.CharField("mas10", null=True, blank=True, max_length=100)
	description = models.CharField('description', max_length=200, null=True, blank=True)
	date_created = models.DateTimeField('date_creat',auto_now_add=True, null=True)
	desc1 = models.TextField('desc1', null=True, blank=True)
	desc2 = models.TextField('desc2', null=True, blank=True)
	desc3 = models.TextField('desc3', null=True, blank=True)
	desc4 = models.TextField('desc4', null=True, blank=True)
	desc5 = models.TextField('desc5', null=True, blank=True)
	desc6 = models.TextField('desc6', null=True, blank=True)
	desc7 = models.TextField('desc7', null=True, blank=True)
	desc8 = models.TextField('desc8', null=True, blank=True)
	desc9 = models.TextField('desc9', null=True, blank=True)
	desc10 = models.TextField('desc10', null=True, blank=True)
	image1 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	image2 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	image3 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	image4 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	image5 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	image6 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	image7 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	image8 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	image9 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	image10 = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)


	image_prod = models.ImageField(default="blank.png",verbose_name="Image", null=True, blank=True)
	#mg = models.ImageField(upload_to='images/', 
	#				height_field=100, width_field=100)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f'/{self.id}'