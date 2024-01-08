from rest_framework import serializers
from my_booking.model.ReviewModel import Review



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'