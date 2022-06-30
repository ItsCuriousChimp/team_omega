from django.contrib import admin
from django.urls import path, include
from .controllers.heartbeat_controller import HeartBeatController
urlpatterns = [
    path('v1/healthcheck', HeartBeatController.health_check),
]
