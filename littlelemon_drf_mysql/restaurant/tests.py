from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import MenuItem, Booking
from django.utils import timezone
from datetime import timedelta

class MenuAPITests(APITestCase):
    def setUp(self):
        self.menu_url = "/api/menu/"
        MenuItem.objects.create(title="Pasta", price="12.50", inventory=10)
        MenuItem.objects.create(title="Pizza", price="9.99", inventory=5)

    def test_list_menu_items(self):
        resp = self.client.get(self.menu_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.json()), 2)

class BookingAPITests(APITestCase):
    def setUp(self):
        self.register_url = "/api/registration/"
        self.token_url = "/api/api-token-auth/"
        self.bookings_url = "/api/bookings/"
        # create user
        self.client.post(self.register_url, {'username': 'alice', 'password': 'pass12345'})
        # get token
        token_resp = self.client.post(self.token_url, {'username': 'alice', 'password': 'pass12345'})
        self.assertEqual(token_resp.status_code, status.HTTP_200_OK)
        self.token = token_resp.json().get('token')
        self.auth_client = APIClient()
        self.auth_client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_create_booking_requires_auth(self):
        data = {{'name': 'Bob', 'no_of_guests': 2, 'booking_date': (timezone.now()+timedelta(days=1)).isoformat()}}
        unauth = self.client.post(self.bookings_url, data, format='json')
        self.assertEqual(unauth.status_code, status.HTTP_401_UNAUTHORIZED)

        auth = self.auth_client.post(self.bookings_url, data, format='json')
        self.assertEqual(auth.status_code, status.HTTP_201_CREATED)

    def test_list_bookings_authenticated(self):
        # create one
        self.auth_client.post(self.bookings_url, {{'name': 'Eve', 'no_of_guests': 4, 'booking_date': (timezone.now()+timedelta(days=2)).isoformat()}}, format='json')
        resp = self.auth_client.get(self.bookings_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(len(resp.json()) >= 1)