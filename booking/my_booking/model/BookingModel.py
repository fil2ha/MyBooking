from datetime import datetime

from django.db import models
from my_booking.models import User
from .RoomsModel import Room


class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь')
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната', related_name='room_id')
    check_in_date = models.DateField(verbose_name='Дата заезда')
    check_out_date = models.DateField(verbose_name='Дата выезда')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
    deleted_at = models.DateField(verbose_name='Дата удаления', null=True, blank=True)
    deleted = models.BooleanField(default=False, verbose_name='Удален')

    def __str__(self):
        return f'Booking {self.id} by {self.user_id}'

    def get_absolute_url(self):
        return f'/profile/'