from django.urls import path
from . import views

urlpatterns = [
    # Ride CRUD API
    path("ride/", views.get_ride, name="ride"),
    path("ride/<str:pk>/", views.get_user_ride, name="user_ride"),
    path("ride/create/", views.createRide, name="create_ride"),
    path("ride/update/<str:pk>/", views.updateRide, name="update_ride"),

    # Booking History API
    path("booking_history/<str:user_id>/", views.get_booking_history, name="booking_history"),
]