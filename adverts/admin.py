from django.contrib import admin
from .models import Advert,AdvertImage
# Register your models here.

class AdvertImagesInline(admin.TabularInline):
    model = AdvertImage

class AdvertAdmin(admin.ModelAdmin):
    inlines = [
        AdvertImagesInline,
    ]
admin.site.register(Advert,AdvertAdmin)