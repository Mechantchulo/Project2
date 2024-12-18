from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from listings.models import PropertyListing  # Assuming you have a PropertyListing model
from django.contrib.auth.decorators import login_required

@login_required
def create_booking(request, property_id):
    """View to create a new booking."""
    property_listing = get_object_or_404(PropertyListing, id=property_id)  # Get the property listing
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # Create a booking instance but don't save to the database yet
            booking.user = request.user  # Set the user to the logged-in user
            booking.save()  # Save the booking to the database
            return redirect('bookings:booking_success')  # Redirect to a success page
    else:
        form = BookingForm(initial={'property_listing': property_listing})  # Pre-fill the form with the property listing
    return render(request, 'bookings/create_booking.html', {'form': form, 'property_listing': property_listing})

def booking_success(request):
    """View to display a success message after booking."""
    return render(request, 'bookings/booking _success.html')
