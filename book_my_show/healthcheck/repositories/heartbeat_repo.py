from ..models.heartbeat_model import HeartBeatDto


class HeartBeatRepository:
    def heartbeat(self) -> HeartBeatDto:
        heart_beat_dto = HeartBeatDto().__str__()
        return heart_beat_dto
