from django import forms
from .models import PropertyListing

class PropertyListingForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = [
            'title', 'description', 'price', 'location', 'property_type', 
            'amenities', 'num_bedrooms', 'num_bathrooms', 'square_footage', 
            'image', 'video', 'virtual_tour_url', 'status', 'tags'
        ]

      