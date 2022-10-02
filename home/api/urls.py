from django.urls import path, include
from classifier.api.urls import router
from .viewsets import instruction_ViewSet, instructionImages_ViewSet
router = router
router.register(r'instruction', instruction_ViewSet)
router.register(r'instructionimages', instructionImages_ViewSet)

urlpatterns = [
    path('', include(router.urls))
]