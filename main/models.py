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



class Purchases(models.Model):
	shop_name = models.CharField("Shop", max_length=100, blank=True)
	def __str__(self):
		return self.shop_name








class Storage(models.Model):
	is_apple = models.BooleanField(default=False, blank=True)
	q_apple = models.IntegerField("Quantity of apples", default=0, blank=True)

	is_banana = models.BooleanField(default=False, blank=True)
	q_banana = models.IntegerField("Quantity of banana", default=0, blank=True)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f'/{self.id}'







class RecipeProduct(models.Model):
	#creator = models.OneToOneField(DimensionsRecipes, null=True, on_delete=models.PROTECT, blank=True)
	emailof_creator = models.CharField('email_creator', max_length=100, blank=True)
	uuid_recipe = models.CharField('uuid', max_length=100, blank=True, null=True)
	CATEGORY = (
		('Горячие блюда','Горячие блюда'), ('Бульоны и супы','Бульоны и супы'), ('Салаты','Салаты'), ('Закуски','Закуски'), ('Выпечка','Выпечка'), ('Десерты','Десерты'), ('Соусы','Соусы'))
	HARDNESS = (
		('Очень легко', 'Очень легко'),('Легко','Легко'),('Средняя сложность','Средняя сложность'),('Нужен опыт','Нужен опыт'),('Сложно','Сложно'),('Очень сложно','Очень сложно'))
	name = models.CharField('name', max_length=250, null=True)
	time = models.CharField('time', max_length=50, null=True)
	adderOf = models.CharField("adderOf", max_length=100, null=True)
	category = models.CharField('category', max_length=200, null=True, choices=CATEGORY)
	hardnessCook = models.CharField('hardness', max_length=200, null=True, choices=HARDNESS)
	ingredient1 = models.CharField('ingredient1', null=True, blank=True, max_length=200)
	ingredient2 = models.CharField('ingredient2', null=True, blank=True, max_length=200)
	ingredient3 = models.CharField('ingredient3', null=True, blank=True, max_length=200)
	ingredient4 = models.CharField('ingredient4', null=True, blank=True, max_length=200)
	ingredient5 = models.CharField('ingredient5', null=True, blank=True, max_length=200)
	ingredient6 = models.CharField('ingredient6', null=True, blank=True, max_length=200)
	ingredient7 = models.CharField('ingredient7', null=True, blank=True, max_length=200)
	ingredient8 = models.CharField('ingredient8', null=True, blank=True, max_length=200)
	ingredient9 = models.CharField('ingredient9', null=True, blank=True, max_length=200)
	ingredient10 = models.CharField('ingredient10', null=True, blank=True, max_length=200)
	mas1 = models.CharField("massa1", null=True, blank=True, max_length=100)
	mas2 = models.CharField("massa2", null=True, blank=True, max_length=100)
	mas3 = models.CharField("massa3", null=True, blank=True, max_length=100)
	mas4 = models.CharField("massa4", null=True, blank=True, max_length=100)
	mas5 = models.CharField("massa5", null=True, blank=True, max_length=100)
	mas6 = models.CharField("massa6", null=True, blank=True, max_length=100)
	mas7 = models.CharField("massa7", null=True, blank=True, max_length=100)
	mas8 = models.CharField("massa8", null=True, blank=True, max_length=100)
	mas9 = models.CharField("massa9", null=True, blank=True, max_length=100)
	mas10 = models.CharField("masssa10", null=True, blank=True, max_length=100)
	description = models.CharField('description', max_length=200, null=True, blank=True)
	date_created = models.DateTimeField('date_creat',auto_now_add=True, null=True)
	desc1 = models.TextField('description1', null=True, blank=True)
	desc2 = models.TextField('description2', null=True, blank=True)
	desc3 = models.TextField('description3', null=True, blank=True)
	desc4 = models.TextField('description4', null=True, blank=True)
	desc5 = models.TextField('description5', null=True, blank=True)
	desc6 = models.TextField('description6', null=True, blank=True)
	desc7 = models.TextField('description7', null=True, blank=True)
	desc8 = models.TextField('description8', null=True, blank=True)
	desc9 = models.TextField('description9', null=True, blank=True)
	desc10 = models.TextField('description10', null=True, blank=True)
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


class AllInterests(models.Model):
	icon = models.CharField(max_length=5, blank=True)
	name = models.CharField(max_length=60, blank=True)
	english = models.CharField(max_length=60, blank=True)

	def __str__(self):
		return self.icon + self.name

class CustomUser(AbstractBaseUser):
	RANKS = (("Початківець","Початківець"),("Професіонал","Професіонал"))
	first_name = models.CharField("first_name", max_length=50, blank=True)
	last_name = models.CharField("last_name", max_length=50, blank=True)
	email = models.CharField("email", max_length=250, unique=True)
	about = models.TextField('about', blank=True)
	amount_of_reciped = models.IntegerField('Recipes amount', default=0)
	interests = models.ManyToManyField(AllInterests, blank=True)
	SEX = (('Чоловіча','male'),('Жіноча','female'))
	username = models.CharField("username", max_length=50, blank=True)
	achievements = models.ManyToManyField(Achievements, blank=True)
	purchases = models.ManyToManyField(Purchases, blank=True)
	sex = models.CharField('Стать', max_length=200, null=True, choices=SEX, blank=True)
	date_joined = models.DateTimeField('date_creat',auto_now_add=True, null=True)
	date_of_birth = models.DateTimeField('Birthday', null=True, blank=True)
	ip_adress = models.CharField('ip_user', max_length=200, null=True, blank=True)
	rank = models.CharField('rank', max_length=200, null=True, choices=RANKS, blank=True, default=RANKS[0][0])
	rank_percentage = models.IntegerField("Percents rank", default=15, blank=True)
	image_profile = models.ImageField( default="default_cook.png", verbose_name="Image", null=True, blank=True)
	my_recipes = models.ManyToManyField(RecipeProduct, blank=True)
	access_to_data = models.BooleanField(default=False)
	is_user = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	#ADD FIELDS WITH PERSONAL PREFERENCES

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['access_to_data', 'password']
	objects = MyAccountManager()
	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True



class Subscribtion(models.Model):
	user = models.OneToOneField(CustomUser, blank=True, on_delete=models.PROTECT)
	followed_by = models.ManyToManyField(CustomUser, blank=True, related_name='followed_by')
	following = models.ManyToManyField(CustomUser, blank=True, related_name='following')
	likedPosts = models.ManyToManyField(RecipeProduct, blank=True, related_name='likedPosts')
	def __str__(self):
		return self.user.email

class PostLike(models.Model):
	post = models.OneToOneField(RecipeProduct, blank=True, on_delete=models.PROTECT)
	usersLiked = models.ManyToManyField(CustomUser, blank=True)

	def __str__(self):
		return self.post.name


class Example(models.Model):
	my_products = models.ManyToManyField(RecipeProduct, blank=True)
	user2 = models.OneToOneField(CustomUser, blank=True, on_delete=models.PROTECT, null=True)
