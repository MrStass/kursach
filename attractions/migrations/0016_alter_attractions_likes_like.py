# Generated by Django 4.0.5 on 2022-06-17 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attractions', '0015_attractions_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like_attractions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attractions.attractions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
