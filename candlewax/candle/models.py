from django.db import models
from django.urls import reverse


class Candle(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    vendor_code = models.IntegerField(verbose_name='Артикул')
    compound = models.CharField(max_length=255, verbose_name='Состав')
    burn_time = models.CharField(max_length=255, blank=True, verbose_name='Время горения')
    size = models.CharField(max_length=255, blank=True, verbose_name='Размеры')
    weight = models.CharField(max_length=255, verbose_name='Вес')
    amount = models.CharField(max_length=255, verbose_name='Кол-во в коробке')
    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts', kwargs={'post_id': self.pk})