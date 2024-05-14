from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_routes),
    path("user/", views.get_user),
]