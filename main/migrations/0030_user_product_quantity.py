# Generated by Django 3.1.7 on 2021-04-11 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_all_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_product_quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(blank=True, default=0, verbose_name='Quantity')),
                ('nameUa', models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.PROTECT, to='main.all_product')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
