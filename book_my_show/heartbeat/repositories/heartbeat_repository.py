from datetime import datetime
from book_my_show.heartbeat.dtos.heartbeat_dto import HeartbeatDto


class HeartbeatRepository:
    def get_heartbeat(self) -> HeartbeatDto:
        heartbeat = HeartbeatDto(datetime.now())
        return heartbeat
