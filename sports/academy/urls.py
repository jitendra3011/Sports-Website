from django.urls import path
from . import views

urlpatterns = [
    path('academy',views.academy ,name="academy")
]