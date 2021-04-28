from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def profile(request):
    check = "works"
    return render(request, 'accounts/profile.html',{'check':check})
