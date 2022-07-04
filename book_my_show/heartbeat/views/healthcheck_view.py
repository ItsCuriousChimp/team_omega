import json
from django.http import JsonResponse
from ..services.healthcheck_service import HealthCheckService


class HealthCheckView:
    def get_healthcheck(request):
        healthcheck_service = HealthCheckService()
        last_beat_at = healthcheck_service.get_health()
        return JsonResponse({"beat": last_beat_at})
