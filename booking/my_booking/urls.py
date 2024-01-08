from django.urls import path, include
from my_booking.views.HotelListView import HotelList, view_hotels
from my_booking.views.RoomsListView import view_rooms, RoomList, view_room
from my_booking.views.ReviewView import ReviewList, post_review
from my_booking.views.UsersView import RegisterUser, LoginUser, logout_user, view_information_about_user, UpdateBooking, UpdateUser
from my_booking.views.AdminPanelView import UpdateHotel, show_hotels, create_hotel, create_room, show_rooms, UpdateRoom, \
    show_booking, show_users, UpdateUserAdmin
from my_booking.views.BookingView import BookingList
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'room', RoomList)
router.register(r'hotel', HotelList)
router.register(r'booking', BookingList)
router.register(r'booking', BookingList)
router.register(r'review', ReviewList)

urlpatterns = [
    path('api/v1/', include(router.urls), name='api'),
    path('', view_hotels, name='home'),
    path('hotel/<int:pk>', view_rooms, name='view_rooms'),
    path('room/<int:pk>', view_room, name='view_room'),
    path('profile/review/<int:pk>', post_review, name='post_review'),
    path('profile/', view_information_about_user, name='view_about_user'),
    path('<int:pk>/update/', UpdateBooking.as_view(), name='update_booking'),
    path('<int:pk>/update_user/', UpdateUser.as_view(), name='update_user'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('hotels', show_hotels, name='show_hotels'),
    path('<int:pk>/update_hotel/', UpdateHotel.as_view(), name='update_hotel'),
    path('hotels/create', create_hotel, name='create_hotel'),
    path('<int:pk>/update_room/', UpdateRoom.as_view(), name='update_room'),
    path('rooms', show_rooms, name='show_rooms'),
    path('roomss/create', create_room, name='create_room'),
    path('bookings', show_booking, name='show_booking'),
    path('users', show_users, name='show_users'),
    path('<int:pk>/update_user_admin/', UpdateUserAdmin.as_view(), name='update_user_admin'),
]