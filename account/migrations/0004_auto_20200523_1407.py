# Generated by Django 3.0.6 on 2020-05-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200522_0610'),
        ('account', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, to='news.Category'),
        ),
        migrations.AlterField(
            model_name='user',
            name='history',
            field=models.ManyToManyField(blank=True, related_name='history', to='news.Article'),
        ),
        migrations.AlterField(
            model_name='user',
            name='saved_articles',
            field=models.ManyToManyField(blank=True, related_name='saved_articles', to='news.Article'),
        ),
    ]