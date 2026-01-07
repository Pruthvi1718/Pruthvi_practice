from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.home, name="index"),
    path("about/", views.about, name="index"),
    path("contact/", views.contact, name="index"),
    path("blog/", views.blog, name="index"),
    path("vk/", views.vk, name="index"),
]
