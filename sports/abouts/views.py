from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def about(request):
    return render(request,'about.html')
