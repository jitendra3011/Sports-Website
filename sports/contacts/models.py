from django.db import models

# Create your models here.
class contacts(models.Model):
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=30, null=True)
    phone_number = models.CharField(max_length=20,null=True)
    message = models.TextField(max_length=1000,null=True)