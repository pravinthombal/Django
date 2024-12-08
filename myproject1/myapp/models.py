from django.db import models
from django.contrib.auth.models import User

# class User(AbstractUser):  # extending Django's default user model
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"