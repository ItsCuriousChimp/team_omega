from book_my_show.coreapis.models.booking_model import Booking
from abc import ABC, abstractmethod  # Built in. No install needed.


class IBookingRepository(ABC):
    @abstractmethod
    def book_seat_by_show_time_id(self):
        pass


class BookingRepository(IBookingRepository):
    def book_seat_by_show_time_id(
        self, user_id: str, show_time_id: str, seat_id: str
    ) -> None:
        booking = Booking.objects.create_booking(user_id, show_time_id, seat_id)
        booking.save()
