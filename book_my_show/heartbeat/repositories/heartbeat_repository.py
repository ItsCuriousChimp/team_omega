from datetime import datetime
from django.utils import timezone
from ..dto.heartbeat_dto import HeartBeatDto


class HeartBeatRepository:
    def heart_beat() -> HeartBeatDto:
        heart_beat_dto = HeartBeatDto(timezone.now())
        return heart_beat_dto
