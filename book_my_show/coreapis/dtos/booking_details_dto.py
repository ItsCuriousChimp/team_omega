class BookingDetailsDto:
    def __init__(
        self,
        show_id: str = None,
        seat_id: str = None,
    ) -> None:
        self.show_id: str = show_id
        self.seat_id: str = seat_id
