from ..repositories.heartbeat_repo import HeartBeatRepository


class HeartBeatService:
    def get_heartbeat_dto(self):
        heart_beat_dto = HeartBeatRepository()
        return heart_beat_dto.heartbeat()
