from django.contrib import admin
from django.urls import path

# dev_28
# from api.views import hello_world, hello_world_drf, hello_world_json

# dev_29
from .views import base_views, product_views, category_views

app_name = "api"

urlpatterns = [
    # path("hello-world/", base_views.hello_world),  # dev_28
    # path("hello-world-json/", base_views.hello_world_json),  # dev_28
    # path("hello-world-drf/", base_views.hello_world_drf),  # dev_28
    # http://127.0.0.1:8000/api/products/
    # 방식       url             기능
    # GET       products/       list
    # POST      products/       create
    # GET       products/{id}   product
    # PUT       products/{id}   modify product
    # DELETE    products/{id}   delete product
    path("products/", product_views.products_api),  # dev_29 : product_views.py
    path("product/<int:pk>/", product_views.product_api),  # dev_30
    # path("categories/", category_views.categories_api),  # dev_30
    path("categories/", category_views.CategoriesAPI.as_view()),  # dev_35
]
