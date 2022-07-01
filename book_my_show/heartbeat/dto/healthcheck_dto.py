from datetime import datetime
from django.db import models
from django.forms import DateTimeField


class HealthCheckDto():
    last_beat_at: datetime

    def __init__(self, last_beat_at: datetime):
        self.last_beat_at = last_beat_at
