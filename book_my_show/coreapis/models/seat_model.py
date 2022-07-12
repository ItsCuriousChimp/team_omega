from django.db import models

from book_my_show.coreapis.models.cinema_screen_model import CinemaScreen
from book_my_show.common.models.base_model import BaseModel

from softdelete.models import SoftDeleteObject


class Seat(BaseModel, SoftDeleteObject):
    seat_no = models.CharField(max_length=8)
    cinema_screen_id = models.ForeignKey(CinemaScreen, on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.cinema_screen_id) + " " + str(self.seat_no))
