from django.db import models
from django.db.models.fields.related import ForeignKey, ForeignObject
from django.contrib.auth.models import User
# Create your models here.
class Advert(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 300)
    description = models.TextField()

class AdvertImage(models.Model):
    advert = ForeignKey(Advert, related_name = 'images', on_delete=models.CASCADE)
    image = models.ImageField()