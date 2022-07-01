import json
from django.http import JsonResponse
from ..services.healthcheck_services import HealthCheckServices


class HealthCheckController:
    def health_check(self) -> json:
        healthcheck_service_instance = HealthCheckServices()
        current_dt = healthcheck_service_instance.get_health()
        return JsonResponse({"beat": current_dt})
