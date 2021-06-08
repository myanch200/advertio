from django.urls import path
from .views import profile,user_registration,user_login,user_logout

app_name = "accounts"

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('register/', user_registration, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),

    

]
