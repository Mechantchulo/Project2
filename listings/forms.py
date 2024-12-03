from django import forms
from .models import PropertyListing

class PropertyListingForm(forms.ModelForm):
    class Meta:
        model = PropertyListing
        fields = ['title', 'description', 'price', 'location']