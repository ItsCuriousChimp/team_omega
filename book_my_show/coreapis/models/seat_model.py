from django.db import models
from book_my_show.coreapis.models.cinema_screen_model import CinemaScreen
from book_my_show.common.models.base_model import BaseModel


class Seat(BaseModel):
    seat_no = models.CharField(max_length=8)
    cinema_screen_id = models.ForeignKey(CinemaScreen, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(str(self.cinema_screen_id) + " " + str(self.pk))
