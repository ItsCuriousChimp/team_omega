from abc import ABC, abstractmethod
from book_my_show.coreapis.repositories.booking_repository import IBookingRepository
from book_my_show.coreapis.repositories.seats_repository import ISeatRepository
from book_my_show.containers.repo_container import RepositoryContainer
from dependency_injector.wiring import Provide


class IBookingService(ABC):
    @abstractmethod
    def is_seat_available(self):
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def create_booking(self):
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def get_booking_response(self):
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def verify_booking(self):
        raise NotImplementedError("Abstract method not implemented.")


class BookingService(IBookingService):
    def __init__(
        self,
        seat_repository: ISeatRepository = Provide[RepositoryContainer.seat_repository],
        booking_repository: IBookingRepository = Provide[
            RepositoryContainer.booking_repository
        ],
    ) -> None:
        self.seat_repository = seat_repository
        self.booking_repository = booking_repository

    def is_seat_available(
        self,
        showtime_id: str,
        seat_id: str,
    ) -> bool:
        all_seats_of_showtime: list[
            dict
        ] = self.seat_repository.get_available_seats_by_show_time_id(showtime_id)

        if [
            seat_details
            for seat_details in all_seats_of_showtime
            if seat_details["seat_id"] == int(seat_id)
        ]:
            return True
        return False

    def create_booking(
        self,
        user_id: str,
        showtime_id: str,
        seat_id: str,
    ) -> None:
        self.booking_repository.book_seat_by_show_time_id(user_id, showtime_id, seat_id)

    def get_booking_response(
        self,
        seat_available: bool,
        user_id: str,
        show_id: str,
        seat_id: str,
    ) -> dict:
        response_dict = {}

        if seat_available:
            booking_status = "Congratulations! Seat Booked."
            response_dict["Booking Details"] = {
                "Show_id": str(show_id),
                "Seat_Id": str(seat_id),
            }
        else:
            booking_status = "Seat not available"

        response_dict["Status"] = booking_status
        response_dict["User_Details"] = str(user_id)

        return response_dict

    def get_user_id(self, user_auth: str) -> IBookingRepository:
        return self.booking_repository.get_user_id_by_auth_token(user_auth)

    def verify_booking(self, show_id: str, seat_id: str, user_auth: str) -> dict:
        availability = self.is_seat_available(show_id, seat_id)
        user_id = self.get_user_id(user_auth)

        if availability:
            self.create_booking(user_id, show_id, seat_id)

        response_dict = self.get_booking_response(
            availability, user_id, show_id, seat_id
        )

        return response_dict
