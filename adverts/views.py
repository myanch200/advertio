from django.shortcuts import render
from .models import Advert,AdvertImage
# Create your views here.
def advert_details(request,id):
    advert = Advert.objects.get(id = id)
    advert_images = AdvertImage.objects.filter(advert=advert)
    context = {"advert":advert,"advert_images":advert_images}
    return render(request,"adverts/advert_detail.html",context)