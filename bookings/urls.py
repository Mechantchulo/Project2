from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('create/<int:property_id>/', views.create_booking, name='create_booking'),  # URL for creating a booking
    path('success/', views.booking_success, name='booking_success'),  # URL for booking success
]