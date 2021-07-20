from django.shortcuts import render
from .models import Advert,AdvertImage, WishList
# Create your views here.
def advert_details(request,id):
    advert = Advert.objects.get(id = id)
    advert_images = AdvertImage.objects.filter(advert=advert)
    context = {"advert":advert,"advert_images":advert_images}
    return render(request,"adverts/advert_detail.html",context)

def wishlist_page(request):
    wishlist = WishList.objects.get(user = request.user)
    for item in wishlist.adverts.all():
        print(item.title)
    context = {'wishlist':wishlist}
    return render(request,'adverts/wishlist_page.html',context)