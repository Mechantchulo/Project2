from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, CustomPasswordChangeView, login_view, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
    path('login/', login_view, name='login'),  # Using custom login view for additional control
    path('logout/', logout_view, name='logout'),  # Using custom logout view for additional control
]


# urlpatterns = [
#     path('password/change/', CustomPasswordChangeView.as_view(), name='account_change_password'),
#     path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
#     path('signup/', views.signup, name='signup'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout')
# ]