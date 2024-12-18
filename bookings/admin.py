from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'property_listing', 'start_date', 'end_date', 'status')  # Fields to display in admin
    list_filter = ('status',)  # Filter bookings by status
    search_fields = ('user__username', 'property_listing__title')  # Search bookings by user or property title
