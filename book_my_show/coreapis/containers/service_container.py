from dependency_injector import containers, providers

from book_my_show.coreapis.services.cinema_service import CinemaService

from book_my_show.coreapis.services.seats_service import SeatService


class ServiceContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "book_my_show.coreapis.views.cinema_view",
            "book_my_show.coreapis.views.seats_view",
        ],
    )
    # config = providers.Configuration()

    cinema_service = providers.Factory(CinemaService)
    seats_service = providers.Factory(SeatService)
