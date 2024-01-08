from django.forms import ModelForm
from my_booking.model.ReviewModel import Review


class AddReview(ModelForm):
    class Meta:
        model = Review
        fields = ('comment',  'rating')


