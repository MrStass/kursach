# Generated by Django 4.0.5 on 2022-06-13 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0004_alter_attractions_favourite_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_attractions', to='attractions.attractions'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Контроль'),
        ),
    ]