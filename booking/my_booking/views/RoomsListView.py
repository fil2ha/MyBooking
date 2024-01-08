import datetime
from django.shortcuts import render, redirect
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from my_booking.forms.DateForm import DateForm
from my_booking.model.RoomsModel import Room
from my_booking.model.ReviewModel import Review
from my_booking.model.BookingModel import Booking
from my_booking.serializers.RoomsSerializer import RoomSerializer


class RoomList(viewsets.mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               GenericViewSet):
    """API Rooms"""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


def view_rooms(request, pk):
    """Select booking date and show free rooms"""
    review = Review.objects.filter(hotel_id=pk, deleted=False).order_by('-pk')
    if request.method == 'POST':
        form = DateForm(request.POST)
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        request.session['start_book_date'] = start_date
        request.session['end_book_date'] = end_date
        queryset = Room.objects.filter(hotel_id=pk, deleted=False, avalible=True)
        rooms_serializer = RoomSerializer(queryset, many=True)
        rooms = rooms_serializer.data
        rooms = list(rooms)
        books = Booking.objects.all().values()
        for room in rooms:
            for book in books:
                if room['id'] == book['room_id_id'] and (book['check_in_date'] <= start < book['check_out_date'] or
                                                         (book['check_in_date'] <= end <= book['check_out_date']) or
                                                         (start <= book['check_in_date'] and end >= book[
                                                             'check_out_date'])):
                    if room in rooms:
                        rooms.remove(room)
        return render(request, 'room.html', {'rooms': rooms, 'form': form, 'review': review})
    else:
        form = DateForm()
        return render(request, 'choice_date.html', {'form': form, 'review': review})


def view_room(request, pk):
    """view deteil room and user can confirm booking this room"""
    start = request.session['start_book_date']
    end = request.session['end_book_date']
    user = request.user
    room_id = Room.objects.get(id=pk)
    queryset = Room.objects.filter(id=pk, deleted=False, avalible=True)
    room_serializer = RoomSerializer(queryset, many=True)
    room = room_serializer.data
    period = (datetime.datetime.strptime(end, '%Y-%m-%d').date()) - (
        datetime.datetime.strptime(start, '%Y-%m-%d').date())
    period = period.days
    for r in room:
        total_price = period * r['price_pre_night']
    if request.method == 'POST':
        booking = Booking.objects.create(user_id=user, room_id=room_id, check_in_date=start, check_out_date=end)
        return redirect('/')
    return render(request, 'show_room.html', {'room': room, 'total_price': total_price})
