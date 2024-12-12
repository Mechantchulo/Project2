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
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'amenities': forms.Textarea(attrs={'rows': 2}),
            'tags': forms.Textarea(attrs={'rows': 1}),
        }

class PropertyListingSearchForm(forms.Form):
    keyword = forms.CharField(required=False, label='Keyword')
    location = forms.CharField(required=False, label='Location')
    property_type = forms.ChoiceField(choices=PropertyListing.PROPERTY_TYPES, required=False)
    custom_property_type = forms.CharField(required=False, label='Specify Property Type if "Other"')
    min_price = forms.DecimalField(required=False, min_value=0, label='Min Price')
    max_price = forms.DecimalField(required=False, min_value=0, label='Max Price')
    num_bedrooms = forms.IntegerField(required=False, min_value=0, label='Bedrooms')
    num_bathrooms = forms.IntegerField(required=False, min_value=0, label='Bathrooms')

      