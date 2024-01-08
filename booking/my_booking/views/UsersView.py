from django.contrib.auth import logout
from datetime import datetime
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from my_booking.model.BookingModel import Booking
from my_booking.forms.UsersForm import AddUser, LoginUser
from django.contrib.auth.mixins import LoginRequiredMixin
from my_booking.models import User



class RegisterUser(CreateView):
    """register user"""
    form_class = AddUser
    success_url = reverse_lazy('home')
    template_name = 'register.html'


class LoginUser(LoginView):
    """Login user"""
    form_class = LoginUser
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    """logout user"""
    logout(request)
    return redirect('home')


def view_information_about_user(request):
    """show info about user (profile)"""
    user_id = request.user.id
    show_booking = Booking.objects.filter(user_id=user_id, deleted=False).select_related("room_id")
    today = datetime.today()
    day_review = today.strftime('%Y-%m-%d')
    return render(request, 'profile.html', {'bookings': show_booking, 'day_review': day_review})


class UpdateBooking(LoginRequiredMixin, UpdateView):
    """update user's booking in profile"""
    model = Booking
    template_name = 'booking_update.html'
    fields = ['check_in_date', 'check_out_date', 'deleted']
    raise_exception = True


class UpdateUser(LoginRequiredMixin, UpdateView):
    """update user's info in profile"""
    model = User
    template_name = 'user_user_update.html'
    fields = ['username', 'email']
    raise_exception = True








