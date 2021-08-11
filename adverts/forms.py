from django import forms
from .models import Advert, AdvertImage


class AddAdvertForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ['title','description','category','price','currency','location']
        exclude = ['author', 'slug', ]


class AdvertImageForm(forms.ModelForm):
    class Meta:
        model = AdvertImage
        fields = ('image',)



