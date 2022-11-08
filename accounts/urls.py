from django.urls import path, include
from . import views

urlpatterns = [
    path('authenticate/',views.authenticate, name='authenticate'),
    path('credentials/',views.validateCredentials, name='validatecredentials'),
    
]