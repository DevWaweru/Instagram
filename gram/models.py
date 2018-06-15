from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profilepics/', default='Image')
    bio = HTMLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', default='Image')
    image_name = models.CharField(max_length = 50)
    image_caption = HTMLField()
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)