from django.contrib import admin
from .models import plantInformation,classifier, plantInformationImages,tempFileHandler,iasData
# Register your models here.
admin.site.register(plantInformation)
admin.site.register(classifier)
admin.site.register(iasData)
admin.site.register(tempFileHandler)
admin.site.register(plantInformationImages)