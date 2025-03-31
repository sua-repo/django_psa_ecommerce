from django.urls import path
from . import views

app_name = "store"

# dev_1
urlpatterns = [
    path("", views.home, name="home"),  # dev_1
    path("about/", views.about, name="about"),  # dev_8
]
