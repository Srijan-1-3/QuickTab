from dataclasses import field
from django.forms import ModelForm
from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name','address_line1','state','contact','postal_code','email_address']