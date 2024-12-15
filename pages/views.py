from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm  # Assuming you will create a form class

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Create a form instance with the submitted data
        if form.is_valid():  # Check if the form is valid
            # Process the data (e.g., send an email, save to database)
            # For now, we'll just redirect to a success page
            return redirect('success')  # Redirect to a success page after submission
    else:
        form = ContactForm()  # Create an empty form instance for GET requests

    return render(request, 'contact.html', {'form': form})  # Render the contact template with the form
# from django.core.mail import send_mail
# from django.conf import settings


# # Create a view to handle the contact form submission
# def contact_view(request):
#     # Check if the request is a POST request
#     if request.method == 'POST':
#         # Create a form instance and populate it with data from the request
#         form = ContactForm(request.POST)
        
#         # Check if the form is valid
#         if form.is_valid():
#             # Get the form data
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
            
#             # Send an email to the site administrator
#             # send_mail(
#             #     'Contact Form Submission',
#             #     f'Name: {name}\nEmail: {email}\nMessage: {message}',
#             #     settings.EMAIL_HOST_USER,
#             #     [settings.EMAIL_HOST_USER],
#             #     fail_silently=False,
#             # )
            
#             # Redirect the user to the homepage
#             return redirect('home')
    
#     # If the request is not a POST request, create an empty form instance
#     else:
#         form = ContactForm()
    
#     # Render the contact form
#     return render(request, 'contact.html', {'form': form})