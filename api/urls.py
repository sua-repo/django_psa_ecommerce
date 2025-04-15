from django.contrib import admin
from django.urls import path

from api.views import hello_world, hello_world_drf, hello_world_json


app_name = "api"

urlpatterns = [
    path("hello-world/", hello_world),  # dev_28
    path("hello-world-json/", hello_world_json),  # dev_28
    path("hello-world-drf/", hello_world_drf),  # dev_28
]
