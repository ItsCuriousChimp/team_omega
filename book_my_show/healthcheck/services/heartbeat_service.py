from ..repositories.heartbeat_repo import HeartbeatRepository


class HeartbeatService:
    def get_heartbeat(self):
        heartbeat_repository = HeartbeatRepository()
        return heartbeat_repository.get_heartbeat()
