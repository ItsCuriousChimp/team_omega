import json
from django.http import JsonResponse
from ..services.healthcheck_services import HealthCheckServices


class HealthCheckController:
    def health_check(requests) -> json:
        healthcheck_service = HealthCheckServices.get_health()
        return JsonResponse({"beat": healthcheck_service})
