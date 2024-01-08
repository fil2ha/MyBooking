from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Oтель")
    location = models.CharField(max_length=255, verbose_name='Локация')
    description = models.TextField(verbose_name='Описание')
    photos = models.ImageField(blank=True, upload_to='photos_hotel', verbose_name='Фото')
    rating = models.DecimalField(blank=True, default=0, max_digits=2, decimal_places=1, verbose_name='Рейтинг')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
    deleted_at = models.DateField(verbose_name='Дата удаления', null=True, blank=True)
    deleted = models.BooleanField(default=False, verbose_name='Удален')

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return f'/hotels'