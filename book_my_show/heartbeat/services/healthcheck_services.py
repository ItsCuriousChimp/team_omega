from datetime import datetime
from ..repositories.healthcheck_repository import HealthCheckRepository


class HealthCheckServices:
    def get_health() -> datetime:
        heart_beat = HealthCheckRepository.get_heart_beat()
        print(heart_beat)
        dt_string = heart_beat.last_beat_at.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string
