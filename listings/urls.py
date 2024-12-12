from django.urls import path
from .views import listing_create, listing_list, listing_update, listing_delete, listing_detail
from . import views

app_name = 'listings' # Define the namespace

urlpatterns = [
    path('', views.listing_list, name='listings_list'),
    path('create/', listing_create, name='listing_create'),
    path('<int:pk>/update/', listing_update, name='listing_update'),
    path('<int:pk>/delete/', listing_delete, name='listing_delete'),
    path('detail/<int:pk>/', listing_detail, name='listing_detail'),
path('search/', views.property_search, name='property_search'),
]