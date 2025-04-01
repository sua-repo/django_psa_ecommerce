from django.contrib import admin
from django.urls import path

from accounts import views

# dev_9

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_user, name="login_user"),  # dev_9
    path("logout/", views.logout_user, name="logout_user"),  # dev_9
    path("register/", views.register_user, name="register_user"),  # dev_10
]
