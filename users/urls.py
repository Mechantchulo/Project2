from django.urls import path
from .views import register, CustomPasswordChangeView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
]