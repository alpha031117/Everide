from django.urls import path
from . import views

urlpatterns = [
    path("ewallet/<int:pk>/", views.view_wallet, name="view_ewallet"),
]