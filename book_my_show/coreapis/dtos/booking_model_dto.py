from book_my_show.coreapis.dtos.booking_details_dto import BookingDetailsDto

class BookingModelDto:
    def __init__(
        self,
        booking_status: str = None,
        user_details: str = None,
        booking_details_dto: BookingDetailsDto = None,
    ) -> None:
        self.booking_status: str =booking_status
        self.user_details: str = user_details 
        self.booking_details_dto: BookingDetailsDto = booking_details_dto