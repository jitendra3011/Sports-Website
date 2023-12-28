from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def event(request):
    return render(request,'events.html')

# Create your views here.
