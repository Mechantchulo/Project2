from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import LoginForm as AllauthLoginForm, SignupForm as AllauthSignupForm
from .models import CustomUser

# Custom user creation form with Bootstrap styling
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'role')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
            'role': forms.Select(attrs={'class': 'form-control'})
        }

# Custom login form for allauth with Bootstrap styling
class CustomLoginForm(AllauthLoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username or Email'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})

# Custom signup form for allauth with Bootstrap styling
class CustomSignupForm(AllauthSignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
