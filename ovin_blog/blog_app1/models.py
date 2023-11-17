from django.db import models
import os
from uuid import uuid4
import random

def upload_to(instance, filename):
    # Get the file's extension
    ext = filename.split('.')[-1]
    random_number = random.randint(1, 9)
    # Generate a unique filename
    new_filename = f'gallery-image{random_number}.{ext}'
    # Return the path where the file will be uploaded
    return os.path.join('blog_app1/static/images/', new_filename)


# Create your models here.
class ImageModel(models.Model):
    picname = models.TextField(blank=False,null=False)
    image = models.ImageField(upload_to=upload_to)
    # Other fields if needed

    def __str__(self):
        return self.picname if self.picname else f"ImageModel {self.id}"