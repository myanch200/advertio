from django.db import models
from django.contrib.auth.models import  User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from advertio.settings import MEDIA_ROOT

from adverts.models import WishList

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length= 255)
    profile_picture = models.ImageField(default= f'{MEDIA_ROOT}/default.png')
    phone_number = models.CharField(max_length=15)
    wishlist = models.ForeignKey(WishList,on_delete=CASCADE, null= True, blank= True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()