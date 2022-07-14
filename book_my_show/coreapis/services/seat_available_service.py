from book_my_show.coreapis.repositories.seat_available_repository import (
    SeatAvailableRepository,
)


class SeatRepository:
    seat_repository = SeatAvailableRepository()

    def get_seat_available(self, showtime_pk: str):
        seat_available_of_showtime = self.seat_repository.get_seat_available(
            showtime_pk
        )
        return seat_available_of_showtime
