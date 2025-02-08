from collections import UserString
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer
from django.views.generic.edit import FormMixin
import json
from .forms import CustomerForm
from django.views.generic import ListView, DetailView
from .forms import CustomerForm
from django.contrib import messages
from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer


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

def customer_delete(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/list')




































# class CustomerListView(FormMixin, ListView):
#     model = Customer
#     template_name = 'customer_form.html'
#     context_object_name = 'customers'
#     form_class = CustomerForm 

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = self.form_class()  
#         return context

#     def post(self, request, *args, **kwargs):

#         form = self.get_form()
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Customer created successfully')
#             return redirect("customer_list_create")
        

#         print(f'form errors {form.errors}')
#         messages.error(request, 'Correct the errors below')
#         return self.get(request, *args, **kwargs)
    




# class CustomerDetailView(DetailView):
#     model = Customer
#     template_name = 'customer_detail.html'
#     context_object_name = 'customer'
#     form_class = CustomerForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = self.form_class(instance=self.object)
#         return context

#     def post(self, request, *args, **kwargs):
#         customer = self.get_object()
#         form = self.form_class(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#             return redirect('customer_list_create')
#         return self.get(request, *args, **kwargs)

    