from django.db import models
from users.models import CustomUser 

# Create your models here.
class PropertyListing(models.Model):
    realtor = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Property Type
property_type = models.CharField(max_length=50)  # e.g., Residential, Commercial

# Amenities
amenities = models.CharField(max_length=255)  # e.g., Pool, Gym, Parking

# Number of Bedrooms and Bathrooms
num_bedrooms = models.IntegerField()
num_bathrooms = models.IntegerField()

# Square Footage
square_footage = models.IntegerField()

# Images and Videos
image = models.ImageField(upload_to='property_images/', blank=True, null=True)
video = models.FileField(upload_to='property_videos/', blank=True, null=True)

# Virtual Tour URL
virtual_tour_url = models.URLField(blank=True, null=True)

# Status
status = models.CharField(max_length=50, default='Available')  # e.g., Available, Sold

# Tags
tags = models.CharField(max_length=255, blank=True, null=True)  # e.g., "Luxury, Modern"
