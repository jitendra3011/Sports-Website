from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def academy(request):
    return render(request,'academy.html')