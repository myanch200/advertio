from django.shortcuts import redirect, render
from .models import Advert,AdvertImage, WishList
from django.contrib.auth.decorators import login_required

# Create your views here.
def advert_details(request,id):
    advert = Advert.objects.get(id = id)
    advert_images = AdvertImage.objects.filter(advert=advert)
    context = {"advert":advert,"advert_images":advert_images}
    return render(request,"adverts/advert_detail.html",context)
@login_required(login_url='accounts:login')
def wishlist_page(request):
    wishlist = WishList.objects.get(user = request.user)
    for item in wishlist.adverts.all():
        print(item.title)
    context = {'wishlist':wishlist}
    return render(request,'adverts/wishlist_page.html',context)


@login_required(login_url='accounts:login')
def remove_from_wishlist(request,pk):
    wishlist = request.user.wishlist
    item = wishlist.adverts.get(id = pk)
    wishlist.adverts.remove(item)
    return redirect('adverts:wishlist_page')
@login_required(login_url='accounts:login')
def add_to_wishlist(request,pk):
    item = Advert.objects.get(id = pk)
    wishlist = request.user.wishlist
    wishlist.adverts.add(item)
    return redirect('adverts:wishlist_page')