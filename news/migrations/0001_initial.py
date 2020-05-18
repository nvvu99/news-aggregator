# Generated by Django 3.0.5 on 2020-05-06 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('url', models.URLField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'publishers',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('original_url', models.URLField(blank=True, max_length=300)),
                ('thumb', models.URLField(blank=True, max_length=300)),
                ('sapo', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('published_date', models.DateTimeField(blank=True)),
                ('category', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='news.Category')),
                ('publisher', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='news.Publisher')),
            ],
            options={
                'db_table': 'articles',
            },
        ),
    ]
