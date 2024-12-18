from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['property_listing', 'start_date', 'end_date']  # Fields to be included in the form
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),  # Date input for start date
            'end_date': forms.DateInput(attrs={'type': 'date'}),  # Date input for end date
        }