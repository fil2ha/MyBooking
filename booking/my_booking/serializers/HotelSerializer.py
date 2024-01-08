from rest_framework import serializers
from my_booking.model.HotelModel import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


