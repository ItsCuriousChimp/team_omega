from dependency_injector import containers, providers
from book_my_show.coreapis.services import (
    booking_service,
    cinema_service,
    city_service,
    movie_service,
    seats_service,
)


class Services(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "book_my_show.coreapis.views.booking_view",
            "book_my_show.coreapis.views.cinema_view",
            "book_my_show.coreapis.views.city_view",
            "book_my_show.coreapis.views.movie_view",
            "book_my_show.coreapis.views.seats_view",
        ],
    )

    cinema_service = providers.Factory(cinema_service.CinemaService)
    booking_service = providers.Factory(booking_service.BookingService)
    city_service = providers.Factory(city_service.CityService)
    movie_service = providers.Factory(movie_service.MovieService)
    seats_service = providers.Factory(seats_service.SeatService)
