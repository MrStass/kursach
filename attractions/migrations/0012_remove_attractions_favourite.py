# Generated by Django 4.0.5 on 2022-06-15 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0011_alter_comments_attraction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attractions',
            name='favourite',
        ),
    ]
