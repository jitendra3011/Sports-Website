from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def soccer(request):
    return render(request,'soccer.html')

def badminton(request):
    return render(request,'badminton.html')

def basketball(request):
    return render(request,'basketball.html')

def location(request):
    return render(request,'location.html')