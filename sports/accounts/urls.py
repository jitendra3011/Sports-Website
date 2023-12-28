from django.urls import path
from . import views
from .views import ShowProfilePageView, EditProfilePageView

urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(), name="show_profile_page"),
    path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name="edit_profile_page"),
]