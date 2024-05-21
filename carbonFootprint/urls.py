from django.urls import path
from . import views

urlpatterns = [
    path("carbon_footprint/<int:pk>/", views.get_carbon_footprint, name="view_carbon_footprint"),
]