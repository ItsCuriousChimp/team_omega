from django.utils import timezone
from ..dtos.heartbeat_dto import HeartbeatDto


class HeartbeatRepository:
    def fetch_heart_beat(self) -> HeartbeatDto:
        heartbeat_response = HeartbeatDto(timezone.now())
        return heartbeat_response
