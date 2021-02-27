# Generated by Django 3.1.7 on 2021-02-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last_name')),
                ('email', models.CharField(max_length=250, unique=True, verbose_name='email')),
                ('about', models.TextField(verbose_name='about')),
                ('sex', models.CharField(choices=[('Чоловіча', 'male'), ('Жіноча', 'female')], max_length=200, null=True, verbose_name='Стать')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date_creat')),
                ('ip_adress', models.CharField(blank=True, max_length=200, null=True, verbose_name='ip_user')),
                ('access_to_data', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
