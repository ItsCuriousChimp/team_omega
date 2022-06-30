from ..repositories.heartbeat_repo import HeartBeatRepository

class HeartBeatService:
    
    def get_heartbeat_dto():
        heart_beat_dto = HeartBeatRepository.heartbeat()
        return heart_beat_dto 
