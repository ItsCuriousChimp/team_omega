from django.contrib import admin
from django.urls import path, include
from .controllers.healthcheck_controller import HealthCheckController
urlpatterns = [
    path('v1/healthcheck', HealthCheckController.health_check),
]
