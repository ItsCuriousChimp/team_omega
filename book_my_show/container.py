from dependency_injector import containers, providers

from book_my_show.coreapis.services.cinema_service import CinemaService

from book_my_show.coreapis.services.seats_service import SeatService

from book_my_show.coreapis.services.booking_service import BookingService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    cinema_service = providers.Factory(CinemaService)
    seats_service = providers.Factory(SeatService)
    # booking_service = providers.Factory(BookingService)
