from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser, EmailActivation, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')
        

    def save(self, commit=...):
        user: CustomUser = super().save(commit)
        if not hasattr(user, 'profile'):
            profile = Profile.objects.create(user=user)
            profile.save()

        if not user.is_active:
            activation = EmailActivation.objects.create(user=user)
            activation.send_email()
        return user