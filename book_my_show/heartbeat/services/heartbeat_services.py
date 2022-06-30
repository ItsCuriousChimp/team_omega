from ..repositories.heartbeat_repository import HeartBeatRepository


class HeartBeatServices:
    def get_heart_beat():
        heart_beat = HeartBeatRepository.heart_beat()
        return heart_beat.last_beat_at
