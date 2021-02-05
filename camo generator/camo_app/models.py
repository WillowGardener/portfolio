from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=50)
    old_image = models.ImageField(upload_to='images')
    new_image = models.ImageField(default=None)