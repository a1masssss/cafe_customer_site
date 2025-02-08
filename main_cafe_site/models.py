from django.db import models
from django.db.models import Sum
import uuid
from django.utils.text import slugify
from django.db import models

# class CustomerType(models.Model):
#     title = models.CharField(max_length=150)


class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=150)
    # type_of_customer = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)












class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('drinks', 'drinks'),
        ('main_dishes', 'main_dishes'),
        ('dessert', 'dessert'),
        ('fast_food', 'fast_food')
    ]
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    available = models.BooleanField(default=True)

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('in_progress', 'in_progress'),
        ('completed', 'completed'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    @property
    def total_price(self):
        return self.items.aggregate(total=Sum('menuitem__price'))['total'] or 0

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()


