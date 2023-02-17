from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("delete/<int:id>", views.delete_page, name="delete-page")
]
