# Generated by Django 3.1.7 on 2021-03-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210310_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='rank_percentage',
            field=models.IntegerField(default=15, verbose_name='Percents rank'),
        ),
    ]
