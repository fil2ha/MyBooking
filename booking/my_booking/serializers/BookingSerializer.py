from rest_framework import serializers
from my_booking.model.BookingModel import Booking



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'