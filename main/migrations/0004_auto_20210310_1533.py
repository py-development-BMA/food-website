# Generated by Django 3.1.7 on 2021-03-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210310_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(blank=True, max_length=100, verbose_name='Shop')),
            ],
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='is_active',
            new_name='is_user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='amount_of_reciped',
            field=models.IntegerField(default=0, verbose_name='Recipes amount'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='BIrthday'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='achievements',
            field=models.ManyToManyField(blank=True, to='main.Achievements'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc1',
            field=models.TextField(blank=True, null=True, verbose_name='description1'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc10',
            field=models.TextField(blank=True, null=True, verbose_name='description10'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc2',
            field=models.TextField(blank=True, null=True, verbose_name='description2'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc3',
            field=models.TextField(blank=True, null=True, verbose_name='description3'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc4',
            field=models.TextField(blank=True, null=True, verbose_name='description4'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc5',
            field=models.TextField(blank=True, null=True, verbose_name='description5'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc6',
            field=models.TextField(blank=True, null=True, verbose_name='description6'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc7',
            field=models.TextField(blank=True, null=True, verbose_name='description7'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc8',
            field=models.TextField(blank=True, null=True, verbose_name='description8'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='desc9',
            field=models.TextField(blank=True, null=True, verbose_name='description9'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient1'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient10',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient10'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient2'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient3'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient4',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient4'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient5',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient5'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient6',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient6'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient7',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient7'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient8',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient8'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='ingredient9',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ingredient9'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='massa1'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas10',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='masssa10'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='massa2'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='massa3'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='massa4'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas5',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='massa5'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas6',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='massa6'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas7',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='massa7'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas8',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='massa8'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='mas9',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='massa9'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='purchases',
            field=models.ManyToManyField(blank=True, to='main.Purchases'),
        ),
    ]
