import json
from django.http import JsonResponse
from ..services.heartbeat_service import HeartbeatService
# Create your views here.


class HeartbeatView:
    def heartbeat_response(request) -> json:
        last_beat = HeartbeatService().get_heartbeat()
        return JsonResponse({"Last Beat At ": last_beat})
