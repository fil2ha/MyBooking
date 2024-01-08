from django.contrib import admin
from my_booking.model.HotelModel import Hotel
from my_booking.models import User

from my_booking.model.RoomsModel import Room
from my_booking.model.BookingModel import Booking
from my_booking.model.ReviewModel import Review



@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Hotel._meta.fields]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [f.name for f in User._meta.fields]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Booking._meta.fields]

@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Room._meta.fields]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Review._meta.fields]
