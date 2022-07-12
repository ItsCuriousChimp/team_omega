from django.db import models
from book_my_show.authenticate.models.user_model import UserModel
from book_my_show.coreapis.models.seat_model import Seat
from book_my_show.coreapis.models.showtime_model import Showtime
from book_my_show.common.models.base_model import BaseModel

class Booking(BaseModel):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    show_time_id = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return str(str(self.user_id) + " " + str(self.show_time_id))
