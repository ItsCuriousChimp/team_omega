from django.db import models


class BookingManagerService(models.Manager):
    def create_booking(self, user_id, show_time_id, seat_id) -> None:

        booking = self.create(
            user_id=user_id, show_time_id_id=show_time_id, seat_id_id=seat_id
        )

        return booking
