from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_routes, name="routes"),

    # User CRUD API
    path("user/", views.get_user, name="user"),
    path('user/<int:pk>/friends/', views.get_user_friends, name='get_user_friends'),
    path("user/create/", views.createUser, name="create_user"),
    path("user/update/<int:pk>/", views.updateUser, name="update_user"),
    path("user/delete/<int:pk>/", views.deleteUser, name="delete_user"),

    # Driver CRUD API
    path("driver/", views.get_driver, name="driver"),
    path("driver/create/", views.createDriver, name="create_driver"),

    # Login Authentication API
    path("login/", views.login_view, name="login"),

    # Add Friend API
    path("add_friend/", views.add_friend, name="add_friend"),

]