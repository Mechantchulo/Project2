# dashboard/views.py
from django.shortcuts import render
from .models import Property, Inquiry

def dashboard_view(request):
    properties = Property.objects.all()
    inquiries = Inquiry.objects.all()
    context = {
        'properties': properties,
        'inquiries': inquiries,
    }
    return render(request, 'dashboard/dashboard.html', context)from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Property, Inquiry
from .forms import PropertyForm, InquiryForm

@login_required
def dashboard_view(request):
    properties = Property.objects.all()
    inquiries = Inquiry.objects.all()
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        inquiry_form = InquiryForm(request.POST)
        if property_form.is_valid():
            property_form.save()
        if inquiry_form.is_valid():
            inquiry_form.save()
        return redirect('dashboard')
    else:
        property_form = PropertyForm()
        inquiry_form = InquiryForm()
    context = {
        'properties': properties,
        'inquiries': inquiries,
        'property_form': property_form,
        'inquiry_form': inquiry_form,
    }
    return render(request, 'dashboard/dashboard.html', context)