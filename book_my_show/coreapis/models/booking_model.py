from django.db import models
from book_my_show.authenticate.models.user_model import UserModel
from book_my_show.coreapis.models.seat_model import Seat
from book_my_show.coreapis.models.showtime_model import Showtime
from book_my_show.common.models.base_model import BaseModel


class BookingManager(models.Manager):
    def create_booking(self, user_id, show_time_id, seat_id) -> None:
        booking = self.create(
            user_id=user_id, show_time_id=show_time_id, seat_id=seat_id
        )

        return booking


class Booking(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    show_time = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    objects = BookingManager()

    def __str__(self) -> str:
        return str(str(self.user) + " " + str(self.show_time))
