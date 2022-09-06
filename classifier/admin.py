from django.contrib import admin
from .models import plantInformation,classifier,tempFileHandler
# Register your models here.
admin.site.register(plantInformation)
admin.site.register(classifier)
admin.site.register(tempFileHandler)