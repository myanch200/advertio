from django.urls import path
from .views import profile,user_registration,user_login,user_logout,landing_page,check_username

app_name = "accounts"

urlpatterns = [
    path('',landing_page,name="landing"),
    path('profile/', profile, name="profile"),
    path('register/', user_registration, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('check_username/<str:data>/',check_username,name="check_username")

    

]
