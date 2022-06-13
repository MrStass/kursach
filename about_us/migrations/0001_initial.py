# Generated by Django 4.0.5 on 2022-06-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('images', models.ImageField(upload_to='about/', verbose_name='Зображення')),
                ('type', models.CharField(max_length=200)),
                ('motivation', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('power', models.CharField(max_length=200)),
                ('weaknesses', models.TextField(verbose_name='Слабкости')),
            ],
            options={
                'verbose_name': 'Творець',
                'verbose_name_plural': 'Творці',
            },
        ),
    ]
