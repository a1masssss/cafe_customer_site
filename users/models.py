from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True, verbose_name="Birth Date")
    username  = models.CharField(max_length=150, blank= True, null=True, verbose_name='Username')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS  = []

    def __str__(self):
        return self.email
    

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name = 'profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Avatar")
    bio = models.TextField(null = True, blank = True, verbose_name='Biography')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Profile of {self.user.email}'