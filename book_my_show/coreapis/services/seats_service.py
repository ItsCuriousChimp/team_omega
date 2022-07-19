from book_my_show.coreapis.repositories.seats_repository import (
    SeatRepository,
)
from dependency_injector.wiring import inject, Provide
from book_my_show.containers.repo_container import RepositoryContainer


class SeatService:
    @inject
    def get_all_seats(
        self,
        showtime_pk: str,
        seat_repository: SeatRepository = Provide[RepositoryContainer.seat_repository],
    ) -> list[dict]:
        all_seats_of_showtime = seat_repository.get_all_seats_by_show_time_id(
            showtime_pk
        )

        return all_seats_of_showtime

    @inject
    def get_unavailable_seats(
        self,
        showtime_pk: str,
        seat_repository: SeatRepository = Provide[RepositoryContainer.seat_repository],
    ) -> list[dict]:
        unavailable_seat_of_showtime: list[
            dict
        ] = seat_repository.get_unavailable_seats_by_show_time_id(showtime_pk)

        return unavailable_seat_of_showtime

    @inject
    def get_seat_available(
        self,
        showtime_pk: str,
        seat_repository: SeatRepository = Provide[RepositoryContainer.seat_repository],
    ) -> list[dict]:
        available_seat_of_showtime: list[
            dict
        ] = seat_repository.get_available_seats_by_show_time_id(showtime_pk)

        return available_seat_of_showtime

    def get_seat_by_seat_type(self, seat_type, showtime_pk: str) -> list[dict]:

        if not seat_type:
            seats = self.get_all_seats(showtime_pk)
        elif seat_type == "available":
            seats = self.get_seat_available(showtime_pk)
        elif seat_type == "unavailable":
            seats = self.get_unavailable_seats(showtime_pk)

        return seats
