from datetime import datetime
from django.db import models


class HeartBeatDto(models.Model):
    last_beat_at = datetime.now()

    def __str__(self):
        return self.last_beat_at.strftime("%m/%d/%Y, %H:%M:%S")
