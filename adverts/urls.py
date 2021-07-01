from django.urls import path
from .views import advert_details

app_name = "adverts"

urlpatterns = [
    path('details/<int:id>/',advert_details,name="advert_details")

    

]