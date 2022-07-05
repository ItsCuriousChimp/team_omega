from datetime import datetime
from ..dtos.heartbeat_dto import HeartbeatDto


class HeartbeatRepository:
    def get_heartbeat(self) -> HeartbeatDto:
        heartbeat = HeartbeatDto(datetime.now())
        return heartbeat
