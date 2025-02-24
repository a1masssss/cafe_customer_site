from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'dob')


    def save(self, commit=...):
        user = super().save(commit)
        if not hasattr(user, 'profile'):
            profile = Profile.objects.create(user=user)
            profile.save

        return user