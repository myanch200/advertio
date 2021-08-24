from django import forms
from .models import Advert, AdvertImage


class AddAdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'description', 'category', 'price', 'currency', 'location']
        exclude = ['author', 'slug', ]


class AdvertImageForm(forms.ModelForm):
    class Meta:
        model = AdvertImage
        fields = ('image',)


class AdvertSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control'})
