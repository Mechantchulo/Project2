# dashboards/views.py
from django.shortcuts import render, redirect
from listings.models import PropertyListing
from .models import PropertyInquiry
from users.models import CustomUser



def index(request):
    featured_listings = PropertyListing.objects.filter(status='Available').order_by('-created_at')[:5]
    return render(request, 'index.html', {'featured_listings': featured_listings})

# Existing views for dashboards
def admin_dashboard(request):
    
    pass

def realtor_dashboard(request):
    # your code for realtor_dashboard
    pass

def user_dashboard(request):
    # your code for user_dashboard
    pass
