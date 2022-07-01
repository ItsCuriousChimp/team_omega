from datetime import datetime
from ..dto.healthcheck_dto import HealthCheckDto


class HealthCheckRepository:
    def get_heart_beat() -> HealthCheckDto:
        heart_beat_dto = HealthCheckDto(datetime.now())

        return heart_beat_dto
