from .models import Customer, MenuItem, Order, OrderItem
from django import forms 
from django.core.exceptions import ValidationError
import re 

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number']
        labels = { 
            'name': 'Name',
            'email': 'Email',
            'phone_number': 'Phone', 
            # 'type_of_customer': 'Customer Type',
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields =['name', 'description', 'price', 'category', 'available']
        labels = { 
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'category': 'Category',
            'available': 'Available',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)





class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'items', 'status']
        labels = {
            'customer': 'Customer',
            'items': 'Items',
            'status': 'Status',
        }
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['status'].required = False


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'menu_item']
        labels = {
            'order': 'Order',
            'menu_item': 'Menu Item',
        }
    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['menu_item'].required = False
        self.fields['order'].required = False

