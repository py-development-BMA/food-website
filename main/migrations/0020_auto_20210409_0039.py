# Generated by Django 3.1.7 on 2021-04-08 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210407_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribtion',
            name='likedPosts',
            field=models.ManyToManyField(blank=True, related_name='likedPosts', to='main.RecipeProduct'),
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, to='main.recipeproduct')),
                ('usersLiked', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]