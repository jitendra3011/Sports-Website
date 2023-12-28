from django.urls import path
from . import views

"""
If we want to see templates in django we want to change settings.py. we can add some path 
in TEMPLATES Dir[].

If we want to one page content add into the other page content we can achieve it from
{% block content %} and {% endblock %} and on which page you want content we can write 
{% extend 'file name'%}

we can create a static file for the project. In the settings.py file we can write from
where you will get static files, how do you refer it, and which folder you can add it.
and at which file we want that changes we can write on {% load static %} in the upper
side of html file.

Database(postgre):- 
DYNAMIC PAGES IN HTML:- 


"""
urlpatterns = [
    path('',views.index,name="index")
]
