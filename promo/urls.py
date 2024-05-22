from django.urls import path
from . import views

urlpatterns = [
    path("promo/", views.view_promo, name="view_ewallet"),
    path("allocate_rewards/<int:user>/", views.allocate_rewards, name="allocate_rewards")
]