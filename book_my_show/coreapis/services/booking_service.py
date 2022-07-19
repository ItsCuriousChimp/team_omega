from book_my_show.coreapis.repositories.booking_repository import BookingRepository

from book_my_show.coreapis.repositories.seats_repository import SeatRepository
from book_my_show.repo_container import RepositoryContainer
from dependency_injector.wiring import inject, Provide
from dependency_injector import containers, providers


class BookingService:
    # seat_repository = SeatRepository()
    # booking_repository = BookingRepository()
    @inject
    def is_seat_available(
        self,
        showtime_pk: str,
        seat_pk: str,
        seat_repository: SeatRepository = Provide[RepositoryContainer.seat_repository],
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

    def create_booking(
        self,
        user_id: str,
        showtime_id: str,
        seat_id: str,
        booking_repository: BookingRepository = Provide[
            RepositoryContainer.booking_repository
        ],
    ) -> None:
        booking_repository.book_seat_by_show_time_id(user_id, showtime_id, seat_id)


class ResponseMaker:
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
