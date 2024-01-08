from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from my_booking.model.RoomsModel import Room



class RoomSerializer(ModelSerializer):
    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')

    def create(self, validated_data):
        raise NotImplementedError('`create()` must be implemented.')



    class Meta:
        model = Room
        fields = '__all__'