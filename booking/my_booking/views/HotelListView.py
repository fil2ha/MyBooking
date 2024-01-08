from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from my_booking.model.HotelModel import Hotel
from my_booking.serializers.HotelSerializer import HotelSerializer


class HotelList(viewsets.mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    """API hotels"""
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


def view_hotels(request):
    """show list hotel"""
    queryset = Hotel.objects.filter(deleted=False).order_by('-rating')
    hotels_serializer = HotelSerializer(queryset, many=True)
    hotels = hotels_serializer.data
    return render(request, 'main.html', {'hotels': hotels})
