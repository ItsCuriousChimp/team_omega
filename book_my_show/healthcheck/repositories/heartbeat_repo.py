from ..models.heartbeat_model import HeartBeatDto

class HeartBeatRepository:
    def heartbeat() -> HeartBeatDto:
        # heart_beat = HeartBeat.Object.get()
        heart_beat_dto = HeartBeatDto().__str__()
        # heart_beat_dto.last_beat_at = heart_beat.last_beat_at
        return heart_beat_dto
