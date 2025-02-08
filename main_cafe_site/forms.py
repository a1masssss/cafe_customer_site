from .models import Customer
from django import forms 

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