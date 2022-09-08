from django.urls import path, include
from . import views
urlpatterns = [
    path('classifier/', views.classifier, name='classifier'),
    path('classifier/filter/',views.filter_files, name='filter_files'),
    path('classifier/classify/',views.classify_files, name='classify_files'),
    path('classifier/results/<int:pk>',views.results, name='results_files'),
    

    # API
    path('api/',include('classifier.api.urls'))
]   