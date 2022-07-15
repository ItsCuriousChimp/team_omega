from book_my_show.coreapis.models.booking_model import Booking


class BookingRepository:
    def book_seat_by_show_time_id(self, user_id, show_time_id, seat_id):
        booking = Booking.objects.create_booking(user_id, show_time_id, seat_id)
        booking.save()
