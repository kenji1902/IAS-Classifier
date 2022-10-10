from django.urls import path, include
from . import views
import database

urlpatterns = [
    path('',views.viewDatabase, name='viewdatabase'),
    path('<int:pk>/',views.viewPlant, name='viewPlant')
    
]
handler404 = 'database.views.handler404'
