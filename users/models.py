from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission 

# Create your models here.
class CustomUser (AbstractUser ):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('realtor', 'Realtor'),
        ('user', 'User '),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    groups = models.ManyToManyField(Group, related_name='customuser_set') 
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions_set')