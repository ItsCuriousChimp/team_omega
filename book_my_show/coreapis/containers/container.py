# from book_my_show.coreapis.services.booking_service import BookingService

from dependency_injector import containers, providers

# from book_my_show.coreapis.services.booking_service import BookingService
from book_my_show.coreapis.services.cinema_service import CinemaService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["book_my_show.coreapis.views.cinema_view"]  # or "users" in your case
    )
    config = providers.Configuration()

    service = providers.Factory(CinemaService)
