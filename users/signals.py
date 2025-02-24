from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser, Profile
from django.conf import settings


@receiver(post_save, sender = CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Profile Created')



@receiver(post_save, sender = settings.AUTH_USER_MODEL)

def save_profile(sender, instance, **kwargs):
    instance.profile.save()