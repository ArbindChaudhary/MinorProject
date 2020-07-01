from django.urls import path
#from .views import UserApiView
from . import views

urlpatterns = [
    path('registration/', views.register, name="registration"),
    path('register/', views.registerUser, name="submitbtn")


]
