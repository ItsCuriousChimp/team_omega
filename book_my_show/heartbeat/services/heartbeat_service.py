from book_my_show.heartbeat.dtos.heartbeat_dto import HeartbeatDto
from book_my_show.heartbeat.repositories.heartbeat_repository import HeartbeatRepository


class HeartbeatService:
    def get_heartbeat(self) -> HeartbeatDto:

        heartbeat_repository = HeartbeatRepository()
        heartbeat = heartbeat_repository.get_heartbeat()
        return heartbeat
