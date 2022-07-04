from datetime import datetime


class HeartbeatDto:
    def __init__(self):
        self.last_beat_at = datetime.now()

    def __str__(self):
        return self.last_beat_at.strftime("%m/%d/%Y, %H:%M:%S")
