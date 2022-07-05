from django.utils import timezone
from ..dtos.heartbeat_dto import HeartbeatDto


class HeartbeatRepository:
    def fetch_heart_beat(self) -> HeartbeatDto:
        get_beat = HeartbeatDto(timezone.now())
        return get_beat
