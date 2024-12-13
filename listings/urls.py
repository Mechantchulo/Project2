from django.urls import path

from . import views
from .views import listing_list, listing_create, listing_update, listing_delete, listing_detail, listing_filter, \
    property_search

app_name = 'listings'
urlpatterns = [
    path('', views.listing_list, name='listings_list'),
    path('', listing_list, name='listing_list'),  # Home page showing all listings
    path('create/', listing_create, name='listing_create'),  # Create a new listing
    path('update/<int:pk>/', listing_update, name='listing_update'),  # Update an existing listing
    path('delete/<int:pk>/', listing_delete, name='listing_delete'),  # Delete a listing
    path('<int:pk>/', listing_detail, name='listing_detail'),  # View details of a listing
    path('filter/<str:sale_status>/', listing_filter, name='listing_filter'),  # Filter listings by sale status
    path('search/', property_search, name='property_search'),  # Search listings
]
