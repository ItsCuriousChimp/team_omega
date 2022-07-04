from datetime import datetime
from ..repositories.healthcheck_repository import HealthCheckRepository


class HealthCheckService:
    def get_health(self) -> datetime:
        healthcheck_repository = HealthCheckRepository()
        heart_beat = healthcheck_repository.get_heart_beat()
        dt_string = heart_beat.last_beat_at.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string
