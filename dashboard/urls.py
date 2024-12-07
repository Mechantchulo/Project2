from django.urls import path
from .views import admin_dashboard, realtor_dashboard, user_dashboard, dashboard_view

app_name = 'dashboard' # Define the namespace

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('realtor/', realtor_dashboard, name='realtor_dashboard'),
    path('user/', user_dashboard, name='user_dashboard'),
]