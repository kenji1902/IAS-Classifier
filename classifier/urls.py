from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.classifier, name='classifier'),
    path('filter/',views.filter_files, name='filter_files'),
    path('classify/',views.classify_files, name='classify_files'),
    path('results/<int:pk>',views.results, name='results_files'),
    path('modifyresults/',views.modifyResult, name='modify_result'),
    
]   

handler403 = 'classifier.views.handler403'


