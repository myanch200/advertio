from django import forms
from .models import Advert, AdvertImage


class AddAdvertForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = '__all__'
        exclude = ['author', 'slug', ]


class AdvertImageForm(forms.ModelForm):
    class Meta:
        model = AdvertImage
        fields = ('image',)



