# Generated by Django 3.0.6 on 2020-05-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200507_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user-avatar/'),
        ),
    ]