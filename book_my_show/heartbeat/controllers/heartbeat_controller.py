import json
from django.http import JsonResponse
from ..services.heartbeat_services import HealthCheckServices


class HeartBeatController:
    # health_check_service = HealthCheckServices

    def health_check(requests) -> json:
        healthcheck_service = HealthCheckServices.get_heart_beat()
        return JsonResponse({"beat": healthcheck_service})
