from django.db import models


class Region(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField('Зображення', upload_to="regions/")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Регіон'
        verbose_name_plural = 'Регіони'


class Country(models.Model):
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    images = models.ImageField('Зображення', upload_to="сountries/")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Держава'
        verbose_name_plural = 'Держави'