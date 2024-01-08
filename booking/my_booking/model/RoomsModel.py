from django.db import models
from .HotelModel import Hotel


class Room(models.Model):
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Отель')
    room_type = models.TextField(verbose_name='Тип комнаты')
    photos = models.ImageField(blank=True, upload_to='photos_hotel', verbose_name='Фото')
    price_pre_night = models.FloatField(blank=True, verbose_name='Цена за ночь')
    discription = models.TextField(blank=True, verbose_name='Описание')
    avalible = models.BooleanField(default=True, verbose_name='Доступна')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
    deleted_at = models.DateField(verbose_name='Дата удаления', null=True, blank=True)
    deleted = models.BooleanField(default=False, verbose_name='Удален')

    def __str__(self):
        return self.room_type


    def get_absolute_url(self):
        return f'/rooms'