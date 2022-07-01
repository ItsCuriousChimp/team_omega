from datetime import datetime
from ..repositories.heartbeat_repository import HeartBeat_Repository


class Healthcheck_Services:
    # health_check_var = 1 #to be implemented
    def health_check(self) -> datetime:
        call_repositories = HeartBeat_Repository().heartBeat_repository_reponse()
        return call_repositories.last_beat
