from django.urls import path
#from .views import UserApiView
from . import views

urlpatterns = [
    path('display/', views.login, name="display"),
    path('submit/', views.submitUser, name="submitb"),
]
