# Generated by Django 3.1.7 on 2021-04-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20210411_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allproduct',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='allproduct',
            name='added_by',
            field=models.IntegerField(max_length=50, null=True, verbose_name='added_by'),
        ),
    ]
