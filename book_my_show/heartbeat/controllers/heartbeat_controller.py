import json
from django.http import JsonResponse
from ..services.heartbeat_services import Healthcheck_Services
# Create your views here.


class HealthCheck_service:
    def healthcheck_response(request) -> json:
        last_beat = Healthcheck_Services().health_check()
        return JsonResponse({"manish": last_beat})
