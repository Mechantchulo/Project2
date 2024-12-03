from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import CustomUser CreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUser CreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUser CreationForm()
    return render(request, 'registration/register.html', {'form': form})