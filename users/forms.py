from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import LoginForm, SignupForm
from .models import CustomUser 


# Custom user creation form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('username', 'email', 'password1', 'password2', 'role')

# Custom login form for allauth
class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


# Custom signup form for allauth
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
