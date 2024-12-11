from django.urls import path
from .views import CustomPasswordChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]