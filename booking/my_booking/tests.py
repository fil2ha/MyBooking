from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from my_booking.model.HotelModel import Hotel
from my_booking.models import User
from my_booking.serializers.HotelSerializer import HotelSerializer


class HotelserializerTestCase(TestCase):
    def test_ok(self):
        """testing serializer"""
        hotel_1 = Hotel.objects.create(name='Test 1', location='Test adress 1', description='Test description 1')
        hotel_2 = Hotel.objects.create(name='Test 2', location='Test adress 2', description='Test description 2')
        data = HotelSerializer([hotel_1, hotel_2], many=True).data
        expected_data = [
            {
                'id': hotel_1.id,
                'name': 'Test 1',
                'location': 'Test adress 1',
                'description': 'Test description 1',
                'photos': None,
                'rating': '0.0',
                'created_at': '2024-01-07',
                'updated_at': '2024-01-07',
                'deleted_at': None,
                'deleted': False

            },
            {
                'id': hotel_2.id,
                'name': 'Test 2',
                'location': 'Test adress 2',
                'description': 'Test description 2',
                'photos': None,
                'rating': '0.0',
                'created_at': '2024-01-07',
                'updated_at': '2024-01-07',
                'deleted_at': None,
                'deleted': False
            },
        ]
        self.assertEqual(expected_data, data)


class HotelsApiTestCase(APITestCase):
    def setUp(self):
        self.hotel_1 = Hotel.objects.create(name='Test 1', location='Test adress 1', description='Test description 1')
        self.hotel_2 = Hotel.objects.create(name='Test 2', location='Test adress 2', description='Test description 2')
        self.user = User.objects.create(username='test_username')

    def test_get(self):
        """testing GET request"""
        url = reverse('hotel-list')
        response = self.client.get(url)
        serializer_data = HotelSerializer([self.hotel_1, self.hotel_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        """testing POST request"""
        self.assertEqual(2, Hotel.objects.all().count())
        url = reverse('hotel-list')
        data = {
            'name': 'Test create',
            'location': 'Test  create',
            'description': 'Test description create',
        }
        self.client.force_login(self.user)
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Hotel.objects.all().count())

    def test_update(self):
        """testing PUT request"""
        url = reverse('hotel-detail', args=(self.hotel_1.id,))
        data = {
            'name': 'Great hotel',
            'location': self.hotel_1.location,
            'description': self.hotel_1.description,
        }
        self.client.force_login(self.user)
        response = self.client.put(url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.hotel_1.refresh_from_db()
        self.assertEqual('Great hotel', self.hotel_1.name)

