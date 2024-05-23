from django.urls import path
from . import views

urlpatterns = [
    # Ride CRUD API
    path("ride/", views.get_ride, name="ride"),
    path("ride/<int:pk>/", views.get_user_ride, name="user_ride"),
    path("ride/create/", views.createRide, name="create_ride"),
    path("ride/update/<int:pk>/", views.updateRide, name="update_ride"),
    path("ride/delete/<int:pk>/", views.cancelRide, name="delete_ride"),

    # Ride Completion API
    path("ride/complete/<int:pk>/", views.completeRide, name="complete_ride"),

    # Booking History API
    path("booking_history/<int:user_id>/", views.get_booking_history, name="booking_history"),
]