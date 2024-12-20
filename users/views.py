from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomUserCreationForm, CustomLoginForm, CustomSignupForm

# Signup view to handle user registration
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user and log them in
            user = form.save()
            backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user, backend=backend)
            messages.success(request, 'Signup successful.')
            return redirect('home')  # Redirect to home after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


# Custom password change view extending PasswordChangeView
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('account_change_password_done')  # Redirect after password change


# Login view to handle user authentication
def login_view(request):
    # Check if there's a 'next' parameter (used for redirection after login)
    next_url = request.GET.get('next', 'home')  # Default to 'home' if 'next' is not present
    
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, 'Login successful.')
                return redirect(next_url)  # Redirect to 'next' if it exists, else home
            else:
                messages.error(request, 'Invalid username or password.')  # Show error message
    else:
        form = CustomLoginForm()
    
    return render(request, 'account/login.html', {'form': form})


# Logout view to handle user logout
def logout_view(request):
    logout(request)  # Log the user out
    messages.success(request, 'Logout successful.')
    return redirect('login')  # Redirect to login page after logout
