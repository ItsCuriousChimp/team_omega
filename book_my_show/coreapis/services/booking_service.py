from abc import ABC
from book_my_show.coreapis.repositories.booking_repository import IBookingRepository
from book_my_show.coreapis.repositories.seats_repository import ISeatRepository
from book_my_show.containers.repo_container import RepositoryContainer
from dependency_injector.wiring import inject, Provide
from rest_framework.authtoken.models import Token

class IBookingService(ABC):
    def is_seat_available(self):
        pass

    def create_booking(self):
        pass

    def get_booking_response(self):
        pass

    def verify_booking(self):
        pass

class BookingService:
    def __init__(
        self,
        seat_repository: ISeatRepository = Provide[RepositoryContainer.seat_repository],
        booking_repository: IBookingRepository = Provide[
            RepositoryContainer.booking_repository
        ],
    ) -> None:
        self.seat_repository = seat_repository
        self.booking_repository = booking_repository

    @inject
    def is_seat_available(
        self,
        showtime_pk: str,
        seat_pk: str,
    ) -> bool:
        all_seats_of_showtime: list[
            dict
        ] = self.seat_repository.get_available_seats_by_show_time_id(showtime_pk)

        if [
            seat_details
            for seat_details in all_seats_of_showtime
            if seat_details["seat_id"] == int(seat_pk)
        ]:
            return True
        return False

    @inject
    def create_booking(
        self,
        user_id: str,
        showtime_id: str,
        seat_id: str,
    ) -> None:
        self.booking_repository.book_seat_by_show_time_id(user_id, showtime_id, seat_id)

    @inject
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

    def get_user_id(self, user_auth):
        return Token.objects.get(key=user_auth).user
        
    @inject
    def verify_booking(self, show_id, seat_id, user_auth):
        availability = self.is_seat_available(show_id, seat_id)
        user_id = self.get_user_id(user_auth)
        if availability:
            self.create_booking(user_id, show_id, seat_id)

        response_dict = self.get_booking_response(
            availability, user_id, show_id, seat_id
        )

        return response_dict
