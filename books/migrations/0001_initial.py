# Generated by Django 3.2.5 on 2021-07-08 22:53

import books.utils.models_utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publishedYear', models.IntegerField(null=True, validators=[books.utils.models_utils.validate_year])),
                ('publishedMonth', models.IntegerField(null=True, validators=[books.utils.models_utils.validate_month])),
                ('publishedDay', models.IntegerField(null=True, validators=[books.utils.models_utils.validate_day])),
                ('isbn_10', models.CharField(max_length=10, null=True)),
                ('isbn_13', models.CharField(max_length=13, null=True)),
                ('pages', models.IntegerField(null=True)),
                ('cover', models.URLField(null=True)),
                ('authors', models.ManyToManyField(to='books.Author')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.language')),
            ],
        ),
    ]
