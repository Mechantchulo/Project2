from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
# from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('dashboard') # Redirect to dashboard after successful registration
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Adjust as necessary
    else:
        form = UserCreationForm()
    return render(request, 'templates/account/signup.html', {'form': form})


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account_change_password_done') # URL to redirect to after a successful password change
    template_name = 'account/password_change.html'
