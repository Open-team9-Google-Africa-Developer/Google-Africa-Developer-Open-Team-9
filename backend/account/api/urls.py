from django.urls import path
from .views import UserRegister
from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    path("register", UserRegister.as_view(), name="register"),
    path("login", obtain_auth_token, name="login"),
]
