from django.urls import path
from . import views

urlpatterns = [
    path("ride/", views.get_ride),
    path("ride/<str:pk>/", views.get_user_ride),
]