from django.urls import path
from .views import admin_dashboard, realtor_dashboard, user_dashboard

urlpatterns = [
    path('', index, name='home'), 
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('realtor/', realtor_dashboard, name='realtor_dashboard'),
    path('user/', user_dashboard, name='user_dashboard'),
]