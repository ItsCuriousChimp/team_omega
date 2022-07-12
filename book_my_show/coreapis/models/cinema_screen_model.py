from django.db import models
from book_my_show.coreapis.models.cinema_model import Cinema
from book_my_show.common.models.base_model import BaseModel
from softdelete.models import SoftDeleteObject


class CinemaScreen(BaseModel, SoftDeleteObject):
    screen_no = models.IntegerField()
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.cinema_id) + " screen:" + str(self.screen_no))
