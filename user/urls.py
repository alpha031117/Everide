from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_routes, name="routes"),
    path("user/", views.get_user, name="user"),
    path("driver/", views.get_driver, name="driver"),
    path("user/create/", views.create_user, name="create_user"),
    path("driver/create/", views.create_driver, name="create_driver"),
    path("login/", views.login_view, name="login"),
    path("add_friend/", views.add_friend, name="add_friend"),

]