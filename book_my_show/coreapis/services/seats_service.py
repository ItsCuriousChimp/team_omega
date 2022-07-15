from book_my_show.coreapis.repositories.seats_repository import (
    SeatRepository,
)


class SeatService:
    seat_repository = SeatRepository()

    def get_all_seats(self, showtime_pk: str) -> list[dict]:
        all_seats_of_showtime = self.seat_repository.get_all_seats_by_show_time_id(
            showtime_pk
        )

        return all_seats_of_showtime

    def get_unavailable_seats(self, showtime_pk: str) -> list[dict]:
        unavailable_seat_of_showtime: list[
            dict
        ] = self.seat_repository.get_unavailable_seats_by_show_time_id(showtime_pk)

        return unavailable_seat_of_showtime

    def get_seat_available(self, showtime_pk: str) -> list[dict]:
        available_seat_of_showtime: list[
            dict
        ] = self.seat_repository.get_available_seats_by_show_time_id(showtime_pk)

        return available_seat_of_showtime
