from django.contrib import admin

from .models import Property, Inquiry, DashboardActivity

admin.site.register(Property)
admin.site.register(Inquiry)
admin.site.register(DashboardActivity)
