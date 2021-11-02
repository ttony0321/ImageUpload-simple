from shortuuidfield import ShortUUIDField
from django.db import models
import uuid
# Create your models here.


class ImageUpload(models.Model):
    title = ShortUUIDField(null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.title
