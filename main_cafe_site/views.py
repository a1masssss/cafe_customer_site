from collections import UserString
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer

from .forms import CustomerForm
from django.shortcuts import render
from .forms import CustomerForm, MenuItemForm, OrderForm
from .models import Customer, MenuItem, Order, OrderItem


def customer_detail(request):
    context = {'customer_detail_list': Customer.objects.all()}
    return render(request, 'customer_detail.html', context)


def customer_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form  = CustomerForm(instance= customer)

        return render(request, 'customer_form.html', {'form': form})
    
    else: 
        if id == 0:
            form = CustomerForm(request.POST)
        else: 
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST, instance = customer)
        if form.is_valid():
            form.save() 
            return redirect('/list')
        return render(request, 'customer_form.html', {'form': form}) 
    
def customer_delete(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/list')


def search_customers(request):
    """AJAX search for customers."""
    query = request.GET.get('q', '')
    customers = Customer.objects.filter(name__icontains=query) if query else Customer.objects.all()
    return render(request, 'partials/customer_list_partial.html', {'': customers})




# ---------------------------------Menu Item---------------------------------

def menu_item_detail(request):
    context = {'menu_item_detail_list': MenuItem.objects.all()}
    return render(request, 'menu_item_detail.html', context)


def menu_item_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = MenuItemForm()
        else:
            menu_item = MenuItem.objects.get(pk=id)
            form  = MenuItemForm(instance= menu_item)

        return render(request, 'menu_item_form.html', {'form': form})
    
    else: 
        if id == 0:
            form = MenuItemForm(request.POST)
        else: 
            menu_item = MenuItem.objects.get(pk=id)
            form = MenuItemForm(request.POST, instance = menu_item)
        if form.is_valid():
            form.save() 
        return redirect('/menu_item/list')



def menu_item_delete(request, id):
    menu_item = MenuItem.objects.get(pk=id)
    menu_item.delete()
    return redirect('/menu_item/list')
def search_menu_items(request):
    """AJAX search for menu items."""
    query = request.GET.get('q', '')
    menu_items = MenuItem.objects.filter(name__icontains=query) if query else MenuItem.objects.all()
    return render(request, 'partials/menu_list_partial.html', {'menu_item': menu_items})


# ----------Orders----------------


def order_list(request):
    context = {'order_list': Order.objects.all()}
    return render(request, 'order_detail.html', context)


def order_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = OrderForm()
        else:
            order = Order.objects.get(pk=id)
            form  = OrderForm(instance= order)

        return render(request, 'order_form.html', {'form': form})
    
    else: 
        if id == 0:
            form = OrderForm(request.POST)
        else: 
            order = Order.objects.get(pk=id)
            form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save() 
        return redirect('/order/list')


def order_delete(request, id):
    order = Order.objects.get(pk=id)
    order.delete()
    return redirect('/order/list')

def search_orders(request):
    query = request.GET.get('q', '')
    orders = Order.objects.filter(customer__name__icontains=query) if query else Order.objects.all()
    return render(request, 'partials/order_list_partial.html', {'order_list': orders})