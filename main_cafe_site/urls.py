from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_form, name = "customer_insert"),
    path('<int:id>/', views.customer_form, name = "customer_update"),
    path('list/', views.customer_detail, name = "customer_list"),
    path('delete/<int:id>/', views.customer_delete, name = "customer_delete"), 


    # -----------------Menu Item---------------- 
    path('menu_item/', views.menu_item_form, name = "menu_item_insert"), 
    path('menu_item/<int:id>/', views.menu_item_form, name = "menu_item_update"),
    path('menu_item/list', views.menu_item_detail, name = "menu_item_list"),
    path('menu_item/delete/<int:id>/', views.menu_item_delete, name = "menu_item_delete"),



    # -----------------Order----------------


    path('order/', views.order_form, name = "order_insert"),
    path('order/<int:id>/', views.order_form, name = "order_update"),
    path('order/list', views.order_list, name = "order_list"),
    path('order/delete/<int:id>/', views.order_delete, name = "order_delete"),
]
