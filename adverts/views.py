from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.forms import formset_factory

from .models import Advert, AdvertImage, WishList
from django.contrib.auth.decorators import login_required
from .forms import AddAdvertForm, AdvertImageForm


# Create your views here.
def advert_details(request, id):
    advert = Advert.objects.get(id=id)
    advert_images = AdvertImage.objects.filter(advert=advert)
    context = {"advert": advert, "advert_images": advert_images}
    return render(request, "adverts/advert_detail.html", context)


@login_required(login_url='accounts:login')
def wishlist_page(request):
    wishlist = WishList.objects.get(user=request.user)
    for item in wishlist.adverts.all():
        print(item.title)
    context = {'wishlist': wishlist}
    return render(request, 'adverts/wishlist_page.html', context)


@login_required(login_url='accounts:login')
def toggle_to_wishlist(request, pk):
    item = Advert.objects.get(id=pk)
    wishlist = request.user.wishlist
    message = ""
    if item in wishlist.adverts.all():
        wishlist.adverts.remove(item)
        message = "Advert removed"

    else:
        wishlist.adverts.add(item)
        message = "Advert added"

    return JsonResponse({"message": message, "wishlistCount": wishlist.count_adds()})


def get_some_data(request):
    return JsonResponse({'data': 'works'})


@login_required(login_url='accounts:login')
def add_advert(request):
    user = request.user
    form = AddAdvertForm()
    ImageFormSet = formset_factory(AdvertImageForm, extra=3)
    formset = ImageFormSet()
    if request.method == "POST":
        form = AddAdvertForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        images = request.FILES.getlist("new_images")
        if form.is_valid() and formset.is_valid():
            advert = form.save(commit=False)
            advert.author = user
            advert.slug = slugify(advert.title)
            advert.save()
            for f in formset.cleaned_data:
                if f:
                    image = f['image']
                    photo = AdvertImage(advert=advert, image=image)
                    photo.save()

            return redirect("accounts:landing")

    return render(request, "adverts/add_advert.html", {"form": form,"formset":formset})
