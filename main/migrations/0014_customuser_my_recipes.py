# Generated by Django 3.1.7 on 2021-03-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_recipeproduct_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='my_recipes',
            field=models.ManyToManyField(blank=True, to='main.RecipeProduct'),
        ),
    ]
