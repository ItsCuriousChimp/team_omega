from datetime import datetime


class HeartbeatDto:
    def __init__(self, time_stamp: datetime):
        self.last_beat_at = time_stamp
