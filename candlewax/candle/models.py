from django.db import models
from django.urls import reverse


class Candle(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    vendor_code = models.IntegerField(verbose_name='Артикул')
    compound = models.CharField(max_length=255, verbose_name='Состав')
    burn_time = models.CharField(max_length=255, blank=True, verbose_name='Время горения')
    size = models.CharField(max_length=255, blank=True, verbose_name='Размеры')
    weight = models.CharField(max_length=255, verbose_name='Вес')
    amount = models.CharField(max_length=255, verbose_name='Кол-во в коробке')
    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('buy', kwargs={'buy_id': self.pk})

    class Meta:
        verbose_name = 'Таблица товаров'
        verbose_name_plural = 'Таблица товаров'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Info(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('buy', kwargs={'buy_id': self.pk})

    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('buy', kwargs={'buy_id': self.pk})

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Delivery(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('buy', kwargs={'buy_id': self.pk})

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'


class Reviews(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    content = models.TextField(verbose_name='Контент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

