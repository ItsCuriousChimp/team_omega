from ..dtos.heartbeat_dto import HeartbeatDto
from ..repositories.heartbeat_repository import HeartbeatRepository


class HeartbeatService:
    def get_heartbeat(self) -> HeartbeatDto:

        heartbeat_repository = HeartbeatRepository()
        heartbeat = heartbeat_repository.get_heartbeat()
        return heartbeat
