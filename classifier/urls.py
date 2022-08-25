from django.urls import path
from . import views
urlpatterns = [
    path('classifier/', views.classifier, name='classifier'),
    path('classifier/post/',views.upload_files, name='upload_files'),
]