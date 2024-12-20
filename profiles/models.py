from django.db import models
from users.models import CustomUser   # Ensure this imports your CustomUser  model

class Profile(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)  # Use CustomUser  here
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    birth_date = models.DateField(null = True, blank = True)
    location = models.CharField(max_length = 100, null = True, blank = True)

    def __str__(self):
        return self.user.username