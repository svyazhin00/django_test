from django.db import models
from django.urls import reverse


class Newspaper(models.Model):

    title = models.CharField(max_length=255, verbose_name='Наименование') #заголовок
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True) #поле статьи
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name= 'Используемое фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name= 'Время создания')
    time_update = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default=True, verbose_name= 'Статус опубликованности')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_slug':self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Все категории'
        verbose_name_plural = 'Все категории'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index = True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_slug':self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доступные категории'
        verbose_name_plural = 'Доступные категории'
        ordering = ['id']



