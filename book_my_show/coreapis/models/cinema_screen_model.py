from django.db import models
from book_my_show.coreapis.models.cinema_model import Cinema
from book_my_show.common.models.base_model import BaseModel


class CinemaScreen(BaseModel):
    screen_no = models.IntegerField()
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(str(self.cinema) + " screen:" + str(self.screen_no))
