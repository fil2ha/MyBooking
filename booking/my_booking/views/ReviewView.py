from django.shortcuts import render, redirect
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from my_booking.model.ReviewModel import Review
from my_booking.model.HotelModel import Hotel
from my_booking.forms.AddReview import AddReview
from my_booking.serializers.ReviewSerializer import ReviewSerializer


class ReviewList(viewsets.mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    """API Review"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


def post_review(request, pk):
    """Post review after booking"""
    if request.method == 'POST':
        form = AddReview(request.POST)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        user = request.user
        hotel_id = Hotel.objects.get(id=pk)
        review = Review.objects.create(user_id=user, hotel_id=hotel_id, comment=comment, rating=rating)
        return redirect('/')
    else:
        form = AddReview()
        return render(request, 'post_review.html', {'form': form})
