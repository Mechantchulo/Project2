from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from listings.models import PropertyListing
from users.models import CustomUser
from .models import Inquiry
#from .forms import PropertyForm, InquiryForm

@login_required
def admin_dashboard(request):
    """Render the admin dashboard with statistics."""
    total_properties = PropertyListing.objects.count()
    total_users = CustomUser.objects.count()
    context = {
        'total_properties': total_properties,
        'total_users': total_users,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required
def realtor_dashboard(request):
    """Render the realtor dashboard with their specific listings and inquiries."""
    properties = PropertyListing.objects.filter(realtor=request.user)  # Fetch properties associated with the logged-in realtor
    inquiries = Inquiry.objects.filter(property__realtor=request.user)  # Fetch inquiries related to the realtor's properties
    context = {
        'properties': properties,
        'inquiries': inquiries,
    }
    return render(request, 'dashboard/realtor_dashboard.html', context)

@login_required
def user_dashboard(request):
    """Render the user dashboard."""
    search_history = request.user.search_history.all()
    liked_properties = request.user.liked_properties.all()
    recommendations = get_recommendations(request.user)

    context = {
        'search_history': search_history,
        'liked_properties': liked_properties,
        'recommendations': recommendations,
    }
    return render(request, 'dashboard/user_dashboard.html', context)

@login_required
def dashboard_view(request):
    """Render a unified dashboard view depending on user role."""
    if request.user.role == 'admin':
        return admin_dashboard(request)
    elif request.user.role == 'realtor':
        return realtor_dashboard(request)
    else:
        return user_dashboard(request)
