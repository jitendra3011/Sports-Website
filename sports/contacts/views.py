from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from contacts.models import contacts

# Create your views here.
def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']

        user = contacts(email=email,first_name=first_name,last_name=last_name,message=message,phone_number=phone_number)
        user.save()
    return render(request,'contact.html')