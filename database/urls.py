from django.urls import path, include
from . import views
import database

urlpatterns = [
    path('',views.viewDatabase, name='viewdatabase'),
    path('<int:pk>/',views.viewPlant, name='viewPlant'),
    path('votecount/',views.votecount,name='voteCount'),
    path('getvote/<iasdata_id>',views.getvote,name='getvote'),
    path('refreshvotepoints/<int:iasdata_id>',views.refreshvotepoints,name='refreshvotepoints'),
]
handler404 = 'database.views.handler404'
