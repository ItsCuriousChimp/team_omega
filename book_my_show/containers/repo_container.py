from dependency_injector import containers, providers
from book_my_show.coreapis.repositories.cinema_repository import (
    CinemaRepository,
    ICinemaRepository,
)
from book_my_show.coreapis.repositories.booking_repository import (
    BookingRepository,
    IBookingRepository,
)
from book_my_show.coreapis.repositories.city_repository import (
    CityRepository,
    ICityRepository,
)
from book_my_show.coreapis.repositories.movie_repository import (
    IMovieRepository,
    MovieRepository,
)
from book_my_show.coreapis.repositories.seats_repository import (
    ISeatRepository,
    SeatRepository,
)
from book_my_show.authenticate.repositories.user_repository import (
    IUserRepository,
    UserRepository,
)


class RepositoryContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "book_my_show.coreapis.services.cinema_service",
            "book_my_show.coreapis.services.booking_service",
            "book_my_show.coreapis.services.city_service",
            "book_my_show.coreapis.services.movie_service",
            "book_my_show.coreapis.services.seats_service",
            "book_my_show.authenticate.services.user_service",
        ],
    )
    cinema_repository: ICinemaRepository = providers.Factory(CinemaRepository)
    booking_repository: IBookingRepository = providers.Factory(BookingRepository)
    city_repository: ICityRepository = providers.Factory(CityRepository)
    movie_repository: IMovieRepository = providers.Factory(MovieRepository)
    seat_repository: ISeatRepository = providers.Factory(SeatRepository)
    user_repository: IUserRepository = providers.Factory(UserRepository)
