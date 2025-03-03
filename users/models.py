from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from functools import partial

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True, verbose_name="Birth Date")
    is_active = models.BooleanField(default=False)
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
    

get_random_token =  partial(get_random_string, 100) 
    


class EmailActivation(models.Model):
    name = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    token =  models.CharField(max_length=100, unique = True, default=get_random_token)
    is_active = models.BooleanField(default=True)


    def send_email(self):
        subject = 'Activation'
        message = f"Activate your account by following link http://localhost:8000/users/activate/{self.token}/"
        from_email = 'example@mail.com'
        recipient_list = [self.user.email]

        send_mail(subject, message, from_email, recipient_list)

        print("#" * 20)
        print('email sent')
        print("#" * 20)

