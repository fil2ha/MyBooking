import datetime
from django.db.models import Avg
from django.dispatch import receiver
from my_booking.model.BookingModel import Booking
from my_booking.model.RoomsModel import Room
from my_booking.model.ReviewModel import Review
from my_booking.model.HotelModel import Hotel
from django.db.models.signals import pre_save, post_save


@receiver(pre_save, sender=Hotel)
def create_delete_date(sender, instance, **kwargs):
    model = instance
    if model.deleted:
        model.deleted_at = datetime.date.today()



@receiver(pre_save, sender=Booking)
def create_delete_date(sender, instance, **kwargs):
    model = instance
    if model.deleted:
        model.deleted_at = datetime.date.today()


@receiver(pre_save, sender=Room)
def create_delete_date(sender, instance, **kwargs):
    model = instance
    if model.deleted:
        model.deleted_at = datetime.date.today()


@receiver(pre_save, sender=Review)
def create_delete_date(sender, instance, **kwargs):
    model = instance
    if model.deleted:
        model.deleted_at = datetime.date.today()

@receiver(post_save, sender=Review)
def create_delete_date(sender, instance, **kwargs):
    model = instance
    rat = Review.objects.filter(hotel_id=model.hotel_id).aggregate(Avg('rating'))
    hotel_id = model.hotel_id.id
    rating = round(rat['rating__avg'], 1)
    hotel_rating = Hotel.objects.filter(id=hotel_id).update(rating=rating)



