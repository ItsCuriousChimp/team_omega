from datetime import datetime
from ..repositories.heartbeat_repository import HeartBeatRepository


class HealthCheckServices:
    def get_heart_beat() -> datetime:
        heart_beat = HeartBeatRepository.heart_beat()
        return heart_beat.last_beat_at
