from django.urls import path
from users.views import SignUpView, activate_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'users/singin.html', next_page='/'), 
          name = 'login'),
    path('register/', SignUpView.as_view(), name = 'singup'), 
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name = 'logout'), 
    path('activate/str: token/', activate_user, name  ='activate')
]