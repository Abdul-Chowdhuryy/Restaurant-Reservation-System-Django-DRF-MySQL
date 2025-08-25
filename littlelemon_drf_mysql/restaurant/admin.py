from django.contrib import admin
from .models import MenuItem, Booking

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'inventory')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'no_of_guests', 'booking_date')