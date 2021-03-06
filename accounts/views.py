from django.http.response import JsonResponse
from accounts.models import Profile
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from adverts.models import Advert
from advertio.settings import MEDIA_URL
from adverts.forms import AdvertSearchForm

def landing_page(request):
    adverts = Advert.objects.all()
    search_form = AdvertSearchForm()
    context = {
        'adverts': adverts,
        'search_form':search_form

    }
    return render(request, 'accounts/landing_page.html', context)


def user_registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/registration.html', context)


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"{username} logged in successfully.")
                return redirect('accounts:profile')
            else:
                messages.error(request, "Wrong credentials , please try again")
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, f"{request.user.username} logged out")
    return redirect('accounts:profile')


@login_required(login_url='accounts:login')
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    form = ProfileUpdateForm(instance=user_profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid:
            form.save()
            return redirect('accounts:landing')

    context = {'form': form, 'profile': user_profile}
    return render(request, 'accounts/profile.html', context)


def check_username(request, data):
    res = {}
    if not data:
        return JsonResponse({"error": "not valid username"})
    res['exists'] = User.objects.filter(username=data).exists()
    print(res)
    return JsonResponse(res)
