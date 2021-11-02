from django.contrib import admin
from .models import ImageUpload

#from django.db import models
# Register your models here.


admin.site.register(ImageUpload)

##no such table error 발생시 --run-syncdb