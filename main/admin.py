from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Achievements)
admin.site.register(Purchases)
admin.site.register(RecipeProduct)
admin.site.register(Subscribtion)
admin.site.register(PostLike)
