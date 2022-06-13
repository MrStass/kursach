from django.db import models


class About(models.Model):
    name = models.CharField(max_length=200)
    images = models.ImageField('Зображення', upload_to="about/")
    type = models.CharField(max_length=200)
    motivation = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    power = models.CharField(max_length=200)
    weaknesses = models.TextField('Слабкости')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Творець'
        verbose_name_plural = 'Творці'
