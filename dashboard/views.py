# dashboards/views.py
from django.shortcuts import render
from listings.models import PropertyListing

def index(request):
    featured_listings = PropertyListing.objects.filter(status='Available').order_by('-created_at')[:5]
    return render(request, 'index.html', {'featured_listings': featured_listings})

# Existing views for dashboards
def admin_dashboard(request):
    # your code for admin_dashboard
    pass

def realtor_dashboard(request):
    # your code for realtor_dashboard
    pass

def user_dashboard(request):
    # your code for user_dashboard
    pass
