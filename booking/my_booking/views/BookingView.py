from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from my_booking.model.BookingModel import Booking
from my_booking.serializers.BookingSerializer import BookingSerializer


class BookingList(viewsets.ModelViewSet):
    """API Booking"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    http_method_names = ('get', 'post', 'put', 'patch')
    permission_classes = (IsAuthenticatedOrReadOnly,)
