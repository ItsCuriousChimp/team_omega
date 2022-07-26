from abc import ABC, abstractmethod
from book_my_show.coreapis.models.booking_model import Booking
from book_my_show.authenticate.models.user_model import UserModel
from rest_framework.authtoken.models import Token


class IBookingRepository(ABC):
    @abstractmethod
    def book_seat_by_show_time_id(self):
        raise NotImplementedError("Abstract method not implemented.")


class BookingRepository(IBookingRepository):
    def book_seat_by_show_time_id(
        self, user_id: str, show_time_id: str, seat_id: str
    ) -> None:
        booking = Booking.objects.create_booking(user_id, show_time_id, seat_id)
        booking.save()

    def get_user_id_by_auth_token(self, user_auth: str) -> UserModel:
        return Token.objects.get(key=user_auth).user
