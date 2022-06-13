from django.contrib.auth.models import User
from django.db import models


class Attractions(models.Model):
    country = models.ForeignKey('main.Country', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    images = models.ImageField('Зображення', upload_to="attractions/")
    description = models.TextField('Опис')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Пам'ятка"
        verbose_name_plural = "Пам'ятки"


class Comments(models.Model):
    country = models.ForeignKey(Attractions, on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Власник коментаря', blank=True, null=True)
    text = models.TextField('Коментар')
    status = models.BooleanField('')
