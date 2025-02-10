from django.contrib import admin
from .models import Customer, MenuItem,Order, OrderItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','phone_number', 'created_at']
    search_fields = ['name', ]
    ordering = ['-created_at']
    list_filter = ['name', 'created_at','created_at', 'email', 'phone_number'] 


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'available']
    search_fields = ['name', 'category']
    list_filter = ['category','available', 'name']
    ordering = ['name']
    search_fields = ['name', 'category']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'get_items', 'status', 'created_at', 'updated_at']
    search_fields = ['customer', 'status']
    ordering = ['created_at']
    list_filter = ['customer', 'status']

    def get_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])
    get_items.short_description = 'Items'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item',]
    search_fields = ['order', 'menu_item']
    ordering = ['order']
    list_filter = ['order', 'menu_item']








