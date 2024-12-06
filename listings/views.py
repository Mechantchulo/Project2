from django.shortcuts import render, get_object_or_404, redirect
from .models import PropertyListing
from .forms import PropertyListingForm

def listing_create(request):
    if request.method == 'POST':
        form = PropertyListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listings:listings_list')
    else:
        form = PropertyListingForm()
    return render(request, 'listings/listing_form.html', {'form': form})

def listing_list(request):
    listings = PropertyListing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_update(request, pk):
    listing = get_object_or_404(PropertyListing, pk=pk)
    if request.method == 'POST':
        form = PropertyListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listings:listings_list')
    else:
        form = PropertyListingForm(instance=listing)
    return render(request, 'listings/listing_form.html', {'form': form})

def listing_delete(request, pk):
    listing = get_object_or_404(PropertyListing, pk=pk)
    if request.method == 'POST':
        listing.delete()
        return redirect('listings:listings_list')
    return render(request, 'listings/listing_confirm_delete.html', {'listing': listing})