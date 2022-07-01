from datetime import datetime
# Creating models here.


class Health_Check_Dto():
    last_beat: datetime

    def __init__(self, last_beat: datetime):
        self.last_beat = last_beat
