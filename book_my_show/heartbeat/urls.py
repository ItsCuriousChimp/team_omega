from django.urls import path
from .controllers import heartbeat_controller

urlpatterns = [
    path('', heartbeat_controller.HealthCheck_service.healthcheck_response)
]
