# Generated by Django 4.0.5 on 2022-06-17 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0013_attractions_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attractions',
            name='likes',
        ),
    ]
