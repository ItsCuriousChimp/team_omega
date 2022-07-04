from ..dtos.heartbeat_dto import HeartbeatDto


class HeartbeatRepository:
    def get_heartbeat(self) -> HeartbeatDto:
        heartbeat_repository = HeartbeatDto().__str__()
        return heartbeat_repository
