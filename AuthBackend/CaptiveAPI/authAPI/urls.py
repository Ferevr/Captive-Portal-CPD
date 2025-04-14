from django.urls import path
from .views import radius_login_api

urlpatterns = [
    path("login/", radius_login_api, name="radius_login"),
]
