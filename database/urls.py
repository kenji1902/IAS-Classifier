from django.urls import path, include
from . import views
import database

urlpatterns = [
    path('',views.viewDatabase, name='viewdatabase')
]