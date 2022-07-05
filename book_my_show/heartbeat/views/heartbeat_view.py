from django.http import JsonResponse
from ..services.heartbeat_service import HeartbeatService


class HeartbeatView:
    def get_heartbeat(self):
        heartbeat_service = HeartbeatService()
        heartbeat = heartbeat_service.get_heartbeat()
        return JsonResponse(
            {"timestamp": heartbeat.last_beat_at.strftime("%m/%d/%Y, %H:%M:%S")}
        )
