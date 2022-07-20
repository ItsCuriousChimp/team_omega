from abc import ABC
from book_my_show.coreapis.repositories.booking_repository import IBookingRepository
from book_my_show.coreapis.repositories.seats_repository import ISeatRepository
from book_my_show.containers.repo_container import RepositoryContainer
from dependency_injector.wiring import inject, Provide


class IBookingService(ABC):
    def is_seat_available(self):
        pass

    def create_booking(self):
        pass

    def get_booking_response(self):
        pass


class BookingService:
    @inject
    def is_seat_available(
        self,
        showtime_pk: str,
        seat_pk: str,
        seat_repository: ISeatRepository = Provide[RepositoryContainer.seat_repository],
    ) -> bool:
        all_seats_of_showtime: list[
            dict
        ] = seat_repository.get_available_seats_by_show_time_id(showtime_pk)

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
        booking_repository: IBookingRepository = Provide[
            RepositoryContainer.booking_repository
        ],
    ) -> None:
        booking_repository.book_seat_by_show_time_id(user_id, showtime_id, seat_id)

    @inject
    def get_booking_response(self, seat_available, user_id, show_id, seat_id):
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
