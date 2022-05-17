
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=250)
    address_line1 = models.TextField(null=True,blank=True)
    state=models.CharField(max_length=250,null=True,blank=True)
    postal_code = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=50,null=True,blank=True)
    email_address = models.EmailField(null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.name







