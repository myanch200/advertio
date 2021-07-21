from django.urls import path
from .views import advert_details,wishlist_page,remove_from_wishlist,add_to_wishlist

app_name = "adverts"

urlpatterns = [
    path('details/<int:id>/',advert_details,name="advert_details"),
    path('wishlist',wishlist_page,name="wishlist_page"),
    path('wishlist-remove/<int:pk>/',remove_from_wishlist,name='remove_from_wishlist'),
    path('add_to_wishlist/<int:pk>/',add_to_wishlist, name='add_to_wishlist')

    

]