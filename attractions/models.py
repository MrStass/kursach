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