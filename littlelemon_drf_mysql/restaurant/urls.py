from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet, register_user

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet, basename='menu')
router.register(r'bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', register_user, name='registration'),
]