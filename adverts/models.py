from django.db import models
from django.db.models.fields.related import ForeignKey, ForeignObject
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length= 250)
    def __str__(self):
        return self.category_name
    

class Advert(models.Model):
    CURRENCY_OPTIONS = (
        ('USD','USD'),
        ('EUR','EUR'),
        ('GBP','GBP'),
        ('BGN','BGN'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 300)
    description = models.TextField()
    slug = models.SlugField()
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    price = models.DecimalField( decimal_places=2, max_digits=12)
    currency = models.CharField(max_length=250, choices= CURRENCY_OPTIONS)
    location = models.CharField(max_length= 300, default="Glasgow,UK")
    uploaded = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}-{self.author}"
    def get_thumbnail(self):
        return AdvertImage.objects.filter(advert = self.id)[0]
        
    

class AdvertImage(models.Model):
    advert = ForeignKey(Advert, related_name = 'images', on_delete=models.CASCADE)
    image = models.ImageField()
    def __str__(self):
        return f"{self.advert}-{self.image.url}"
    

    
class WishList(models.Model):
    adverts = models.ManyToManyField(Advert)
    user  = models.OneToOneField(User, on_delete= models.CASCADE,null= True, blank= True)

    def __str__(self):
        return f'{self.user.username} - WishList'
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        WishList.objects.create(user=instance)
        
        
    instance.wishlist.save()