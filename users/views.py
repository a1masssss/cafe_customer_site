from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm
from users.models import EmailActivation
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'users/singup.html'


    
def activate_user(request, token:str):
    activation  = EmailActivation.objects.get(token=token)
    activation.is_active = True
    activation.save()
    return redirect('login')
