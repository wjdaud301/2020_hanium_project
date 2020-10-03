from rest_framework import serializers
#from .models import Addresses 
from django.contrib.auth.models import User


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

