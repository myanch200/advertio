from django.core.paginator import Paginator
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.forms import formset_factory
from django.views.generic import ListView

from .models import Advert, AdvertImage, WishList
from django.contrib.auth.decorators import login_required
from .forms import AddAdvertForm, AdvertImageForm, AdvertSearchForm
from django.contrib.postgres.search import TrigramSimilarity


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


@login_required(login_url="accounts:login")
def add_advert(request):
    form = AddAdvertForm()
    if request.is_ajax() and request.method == "POST":
        form = AddAdvertForm(data=request.POST)
        data = {}
        print(request.POST)
        if form.is_valid():
            advert = form.save(commit=False)
            advert.author = request.user
            advert.slug = slugify(advert.title)
            advert.save()
            data['advert_id'] = advert.id
            data['message'] = f"{advert.title} added !"
            return JsonResponse(data)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"message": errors}, status=400)

    return render(request, "adverts/add_advert.html", {"form": form})


"""Consiming the images from dropzone"""
@login_required(login_url="accounts:login")
def dropzone_image(request):
    if request.method == 'POST':
        image = request.FILES.get("file")
        advert = Advert.objects.filter(author=request.user).order_by('-uploaded')[0]
        AdvertImage.objects.create(image=image, advert=advert)
        return JsonResponse({"message": "success"})


def search(request):
    form = AdvertSearchForm()
    results = []
    contex = {}
    if 'q' in request.GET:
        form = AdvertSearchForm(request.GET)
        if form.is_valid():
            page = request.GET.get('page', 1)
            q = form.cleaned_data['q']
            results = Advert.objects.annotate(similarity=TrigramSimilarity('title', q), ).filter(
                similarity__gte=0.05).order_by('-similarity')
            paginator = Paginator(results, 1)
            adverts = paginator.page(page)
            contex = {
                "page_obj":adverts,
                'query': q
            }
            return render(request,'adverts/search.html',contex)
    return render(request, 'adverts/search.html')


