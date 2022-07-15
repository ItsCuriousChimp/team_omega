from book_my_show.coreapis.repositories.booking_repository import BookingRepository
from book_my_show.coreapis.repositories.seats_repository import SeatRepository


class BookingService:
    seat_repository = SeatRepository()
    booking_repository = BookingRepository()

    def is_available(self, showtime_pk: str, seat_pk: str) -> bool:
        all_seats_of_showtime = (
            self.seat_repository.get_available_seats_by_show_time_id(showtime_pk)
        )

        # using list comprehension
        # for seat_to_book in [
        #     seat_details
        #     for seat_details in all_seats_of_showtime
        #     if seat_details["seat_id"] == int(seat_pk)
        # ]:
        #     return True

        if [
            seat_details
            for seat_details in all_seats_of_showtime
            if seat_details["seat_id"] == int(seat_pk)
        ]:
            return True

        return False

    def create_booking(self, user_id, showtime_id, seat_id):
        self.booking_repository.book_seat_by_show_time_id(user_id, showtime_id, seat_id)
