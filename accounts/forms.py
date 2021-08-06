from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


# Profile update form with all field included
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'wishlist']

    field_order = ['profile_picture', 'first_name', 'last_name', 'bio', 'phone_number']
