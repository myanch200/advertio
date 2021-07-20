from django.urls import path
from .views import advert_details,wishlist_page

app_name = "adverts"

urlpatterns = [
    path('details/<int:id>/',advert_details,name="advert_details"),
    path('wishlist',wishlist_page,name="wishlist_page")

    

]