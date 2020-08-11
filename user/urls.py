from user.views import *
from django.urls import path

urlpatterns = [
    path("login/", LoginView.as_view(), name="user_login"),
    path("create/", UserCreate.as_view(), name="user_create"),
]
