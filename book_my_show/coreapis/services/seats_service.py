from abc import ABC, abstractmethod
from book_my_show.coreapis.repositories.seats_repository import ISeatRepository
from dependency_injector.wiring import Provide
from book_my_show.containers.repo_container import RepositoryContainer


class ISeatService(ABC):
    @abstractmethod
    def get_all_seats(self):
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def get_unavailable_seats(self):
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def get_seat_available(self):
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def get_seat_by_seat_type(self):
        raise NotImplementedError("Abstract method not implemented.")


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
