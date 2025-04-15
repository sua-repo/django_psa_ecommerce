from django.contrib import admin
from django.urls import path

# dev_28
# from api.views import hello_world, hello_world_drf, hello_world_json

# dev_29
from .views import base_views, product_views

app_name = "api"

urlpatterns = [
    path("hello-world/", base_views.hello_world),  # dev_28
    path("hello-world-json/", base_views.hello_world_json),  # dev_28
    path("hello-world-drf/", base_views.hello_world_drf),  # dev_28
    # http://127.0.0.1:8000/api/products/
    # 방식 : GET
    # url : products/
    # 기능 : list
    path("products/", product_views.products_api),  # dev_29 : product_views.py
]
