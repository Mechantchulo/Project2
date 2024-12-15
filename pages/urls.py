from django.urls import path
from .views import contact_view

urlpatterns = [
    path('', home_view, name='home'),  # Assuming you have a home view
    path('contact/', contact_view, name='contact'),  # URL for the contact form
]