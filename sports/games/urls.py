from django.urls import path
from . import views

urlpatterns = [
    path('soccer',views.soccer ,name="soccer"),
    path('badminton',views.badminton,name="badminton"),
    path('basketball',views.basketball,name="basketball"),
    path('location',views.location,name="location")
]