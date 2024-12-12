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

class PropertyListingSearchForm(forms.Form):
    keyword = forms.CharField(required=False, label='Keyword')
    location = forms.CharField(required=False, label='Location')
    property_type = forms.ChoiceField(choices=PropertyListing._meta.get_field('property_type').choices, required=False)
    min_price = forms.DecimalField(required=False, min_value=0, label='Min Price')
    max_price = forms.DecimalField(required=False, min_value=0, label='Max Price')
    bedrooms = forms.IntegerField(required=False, min_value=0, label='Bedrooms')
    bathrooms = forms.IntegerField(required=False, min_value=0, label='Bathrooms')

      