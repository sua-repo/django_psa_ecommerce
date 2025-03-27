from django.urls import path
from . import views

# dev_1
urlpatterns = [
    path("", views.home, name="home"),  # dev_1
]
