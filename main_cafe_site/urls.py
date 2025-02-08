from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_form, name = "customer_insert"),
    path('<int:id>/', views.customer_form, name = "customer_update"),
    path('list/', views.customer_detail, name = "customer_list"),
    path('delete/<int:id>/', views.customer_delete, name = "customer_delete"),   
]
