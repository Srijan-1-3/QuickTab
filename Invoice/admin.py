from django.contrib import admin
from .models import Client,Inventory,Invoice
# Register your models here.
admin.site.register(Client)
admin.site.register(Inventory)
admin.site.register(Invoice)

