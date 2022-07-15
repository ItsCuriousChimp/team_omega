from book_my_show.coreapis.repositories.booking_repository import BookingRepository
from book_my_show.coreapis.repositories.seats_repository import SeatRepository


class BookingService:
    seat_repository = SeatRepository()
    booking_repository = BookingRepository()

    def is_seat_available(self, showtime_pk: str, seat_pk: str) -> bool:

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

    def create_booking(self, user_id: str, showtime_id: str, seat_id: str) -> None:
        self.booking_repository.book_seat_by_show_time_id(user_id, showtime_id, seat_id)

    def get_user_name(self, user_id: str) -> dict:
        user_details = self.booking_repository.fetch_user_details_by_user_is(user_id)
        user_detail_dict = {}

        for user in user_details:
            user_detail_dict["User_Id"] = str(user.pk)

        return user_detail_dict
