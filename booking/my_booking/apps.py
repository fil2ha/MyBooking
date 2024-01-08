from django.apps import AppConfig


class MyBookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_booking'

    def ready(self):
        import my_booking.signals
