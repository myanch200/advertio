from django.contrib import admin
from .models import Advert,AdvertImage,Category,WishList
# Register your models here.

class AdvertImagesInline(admin.TabularInline):
    model = AdvertImage

class AdvertAdmin(admin.ModelAdmin):
    inlines = [
        AdvertImagesInline,
    ]
    prepopulated_fields = {"slug":("title",)}
admin.site.register(Advert,AdvertAdmin)
admin.site.register(Category)
admin.site.register(WishList)
