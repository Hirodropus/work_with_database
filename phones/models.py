from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.URLField(max_length=500, verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='SLUG')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ['name']

    def save(self, *args, **kwargs):
        # Всегда устанавливаем slug как слагифицированное значение name
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name