# Generated by Django 3.1.7 on 2021-03-17 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210313_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeproduct',
            name='creator',
        ),
    ]
