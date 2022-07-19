from dependency_injector import containers, providers
from book_my_show.coreapis.repositories.cinema_repository import CinemaRepository
from book_my_show.coreapis.repositories.booking_repository import BookingRepository
from book_my_show.coreapis.repositories.city_repository import CityRepository
from book_my_show.coreapis.repositories.movie_repository import MovieRepository
from book_my_show.coreapis.repositories.seats_repository import SeatRepository


class RepositoryContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "book_my_show.coreapis.services.cinema_service",
            "book_my_show.coreapis.services.booking_service",
            "book_my_show.coreapis.services.city_service",
            "book_my_show.coreapis.services.movie_service",
            "book_my_show.coreapis.services.seat_searvice",
        ],
    )
    cinema_repository = providers.Factory(CinemaRepository)
    booking_repository = providers.Factory(BookingRepository)
    city_repository = providers.Factory(CityRepository)
    movie_repository = providers.Factory(MovieRepository)
    seat_repository = providers.Factory(SeatRepository)
