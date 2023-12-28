from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

"""
When I send request to the server the server first go into the sports website urls from
their it will check the path or app url after that in the app path url we can add a path of
function this function calls in views.py file by giving re  quest and this page show on
browser.

HTTP request methods:- GET, POST, PUT, DELETE, HEAD, CONNECT, OPTION, TRACE, PATCH.
GET AND POST REQUEST:
Get:- When you are expecting from server.
Post:- Adding the new data to the server.
"""
def index(request):

    dest1 = Destination()
    dest1.name = 'Chess'

    return render(request,'index.html',{'dest1': dest1})