from django.http.response import JsonResponse
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
def toggle_to_wishlist(request,pk):
    item = Advert.objects.get(id = pk)
    wishlist = request.user.wishlist
    message = ""
    if item in wishlist.adverts.all():
        wishlist.adverts.remove(item)
        message = "Advert removed"
        
    else:
        wishlist.adverts.add(item)
        message = "Advert added"

        
    return JsonResponse({"message":message})


def get_some_data(request):
    return JsonResponse({'data':'works'})
