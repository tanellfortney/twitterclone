from distutils.errors import LinkError
from django.db import models
from cloudinary.models import CloudinaryField

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=False, null=False, max_length=140, db_index=True
    )
    like = models.IntegerField(
        'Like', blank=True, default=0
    )
    image = CloudinaryField(
        'Image', blank=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True 
    )

# class Image(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='images')

#     def __str__(self):
#         return self.title