from django.http import JsonResponse
from ..services.heartbeat_services import HeartBeatServices


class HeartBeatController:
    def health_check(requests):
        heartbeat = HeartBeatServices.get_heart_beat()
        return JsonResponse({"beat": heartbeat})
