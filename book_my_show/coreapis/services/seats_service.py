from abc import ABC
from book_my_show.coreapis.repositories.seats_repository import ISeatRepository
from dependency_injector.wiring import inject, Provide
from book_my_show.containers.repo_container import RepositoryContainer


class ISeatService(ABC):
    def get_all_seats(self):
        pass

    def get_unavailable_seats(self):
        pass

    def get_seat_available(self):
        pass

    def get_seat_by_seat_type(self):
        pass


class SeatService(ISeatService):
    def __init__(
        self,
        seat_repository: ISeatRepository = Provide[RepositoryContainer.seat_repository],
    ) -> None:
        self.seat_repository = seat_repository

    def get_all_seats(
        self,
        showtime_id: str,
    ) -> list[dict]:
        all_seats_of_showtime = self.seat_repository.get_all_seats_by_show_time_id(
            showtime_id
        )

        return all_seats_of_showtime

    def get_unavailable_seats(
        self,
        showtime_id: str,
    ) -> list[dict]:
        unavailable_seat_of_showtime: list[
            dict
        ] = self.seat_repository.get_unavailable_seats_by_show_time_id(showtime_id)

        return unavailable_seat_of_showtime

    def get_seat_available(
        self,
        showtime_id: str,
    ) -> list[dict]:
        available_seat_of_showtime: list[
            dict
        ] = self.seat_repository.get_available_seats_by_show_time_id(showtime_id)

        return available_seat_of_showtime

    def get_seat_by_seat_type(self, seat_type, showtime_id: str) -> list[dict]:

        if not seat_type:
            seats = self.get_all_seats(showtime_id)
        elif seat_type == "available":
            seats = self.get_seat_available(showtime_id)
        elif seat_type == "unavailable":
            seats = self.get_unavailable_seats(showtime_id)

        return seats
