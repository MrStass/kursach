# Generated by Django 4.0.5 on 2022-06-13 10:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attractions', '0002_attractions_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='favourite',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
