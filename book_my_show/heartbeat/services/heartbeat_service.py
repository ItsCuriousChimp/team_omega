from datetime import datetime
from ..repositories.heartbeat_repository import HeartbeatRepository


class HeartbeatService:
    def get_last_heartbeat(self) -> datetime:
        call_repository = HeartbeatRepository().fetch_heart_beat()
        return call_repository.last_beat
