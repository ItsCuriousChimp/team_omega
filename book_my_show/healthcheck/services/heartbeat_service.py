from ..repositories.heartbeat_repository import HeartbeatRepository


class HeartbeatService:
    def get_heartbeat(self) -> HeartbeatRepository:
        heartbeat_repository = HeartbeatRepository()
        return heartbeat_repository.get_heartbeat()
