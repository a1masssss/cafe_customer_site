from django.contrib import admin
from .models import Customer, MenuItem,Order, OrderItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','phone_number', 'created_at']
    search_fields = ['name',    ]
    ordering = ['-created_at']
    list_filter = ['name', 'created_at', 'phone_number']    
    fieldsets = [
        (
            "Main info", 
            {
                'fields': ['name', 'email'], 
            },
        ),
        (
            'Additional Info',
            {
                'fields': ['phone_number'],
            },
        ),
    ]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass








