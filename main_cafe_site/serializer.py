import io
from rest_framework import serializers
from .models import Customer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'



# class CustomerModel():
#     def __init__(self, name, email, phone_number):
#         self.name = name
#         self.email = email 
#         self.phone_number = phone_number

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=150) 
    phone_number =serializers.CharField(max_length = 17)
    created_at  = serializers.DateTimeField(read_only = True)
    



# def encode():
#     model = Customer('Kazbek', 'kazbek@gmail.com','+77752795080')
#     model_sr = CustomerSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep = '\n')
#     json  = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"name": "Altynai", "email": "altynai@gmail.com", "phone_number": "38439483"}')
#     data = JSONParser().parse(stream)
#     serializer = CustomerSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)


