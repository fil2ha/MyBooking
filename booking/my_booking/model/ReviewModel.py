from django.db import models
from my_booking.models import User
from .HotelModel import Hotel


class Review(models.Model):
    RATING_CHOICE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Отель')
    comment = models.TextField(verbose_name='Отзыв')
    rating = models.PositiveIntegerField(choices= RATING_CHOICE, verbose_name='Рейтинг')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')
    deleted_at = models.DateField(verbose_name='Дата удаления', null=True, blank=True)
    deleted = models.BooleanField(default=False, verbose_name='Удален')

    def __str__(self):
        return self.comment