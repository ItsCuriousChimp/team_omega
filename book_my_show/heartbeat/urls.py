from django.contrib import admin
from django.urls import path
from .views.healthcheck_view import HealthCheckView


urlpatterns = [
    path("", HealthCheckView.get_healthcheck),
]
