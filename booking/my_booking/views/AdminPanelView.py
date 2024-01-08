
from django.shortcuts import redirect, render
from django.views.generic import UpdateView
from my_booking.model.HotelModel import Hotel
from my_booking.model.RoomsModel import Room
from my_booking.model.BookingModel import Booking
from my_booking.forms.AdminPanelForm import AddHotel, AddRoom
from django.contrib.auth.mixins import LoginRequiredMixin
from my_booking.models import User
from my_booking.serializers.HotelSerializer import HotelSerializer
from my_booking.serializers.RoomsSerializer import RoomSerializer


def show_hotels(request):
    """show hotel's list"""
    queryset = Hotel.objects.all().order_by('-rating')
    hotels_serializer = HotelSerializer(queryset, many=True)
    hotels = hotels_serializer.data
    return render(request, 'admin_hotel.html', {'hotels': hotels})


def create_hotel(request):
    """create new hotel"""
    if request.method == 'POST':
        form = AddHotel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/hotels')
    else:
        form = AddHotel()
        return render(request, 'create_hotel.html', {'form': form})


class UpdateHotel(LoginRequiredMixin, UpdateView):
    """update hotel"""
    model = Hotel
    template_name = 'hotel_update.html'
    fields = ['name',  'location', 'description', 'photos', 'deleted']
    raise_exception = True


def show_rooms(request):
    """show all rooms"""
    queryset = Room.objects.all().order_by('hotel_id')
    rooms_serializer = RoomSerializer(queryset, many=True)
    rooms = rooms_serializer.data
    return render(request, 'admin_room.html', {'rooms': rooms})


def create_room(request):
    """create room"""
    if request.method == 'POST':
        form = AddRoom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/rooms')
    else:
        form = AddRoom()
        return render(request, 'create_room.html', {'form': form})


class UpdateRoom(LoginRequiredMixin, UpdateView):
    """update room"""
    model = Room
    template_name = 'room_update.html'
    fields = ['hotel_id',  'room_type', 'discription', 'photos', 'price_pre_night', 'avalible', 'deleted']
    raise_exception = True


def show_booking(request):
    """show all booking"""
    booking = Booking.objects.all().order_by('user_id')
    return render(request, 'admin_booking.html', {'booking': booking})


def show_users(request):
    """show all users"""
    users = User.objects.all().order_by('id')
    return render(request, 'admin_user.html', {'users': users})


class UpdateUserAdmin(UpdateView):
    """update user info"""
    model = User
    template_name = 'user_update.html'
    fields = ['username', 'email', 'is_staff']
    raise_exception = True