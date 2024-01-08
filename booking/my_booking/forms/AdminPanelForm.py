from django.forms import ModelForm
from my_booking.model.HotelModel import Hotel
from my_booking.model.RoomsModel import Room
from my_booking.models import User


class AddHotel(ModelForm):
    class Meta:
        model = Hotel
        fields = ('name',  'location', 'description', 'photos')


class AddRoom(ModelForm):
    class Meta:
        model = Room
        fields = ('hotel_id',  'room_type', 'discription', 'price_pre_night', 'photos')

