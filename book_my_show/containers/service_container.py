from dependency_injector import containers, providers
from book_my_show.authenticate.services.user_service import (
    IUserService, 
    UserService,
)
from book_my_show.coreapis.services.booking_service import (
    IBookingService,
    BookingService,
)
from book_my_show.coreapis.services.cinema_service import (
    ICinemaService,
    CinemaService,
)
from book_my_show.coreapis.services.city_service import (
    ICityService, 
    CityService,
)
from book_my_show.coreapis.services.movie_service import (
    IMovieService, 
    MovieService
)
from book_my_show.coreapis.services.seats_service import (
    ISeatService,
    SeatService,
)


class ServiceContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "book_my_show.coreapis.views.booking_view",
            "book_my_show.coreapis.views.cinema_view",
            "book_my_show.coreapis.views.city_view",
            "book_my_show.coreapis.views.movie_view",
            "book_my_show.coreapis.views.seats_view",
            "book_my_show.authenticate.views.register_user_view",
        ],
    )

    cinema_service: ICinemaService  = providers.Factory(CinemaService)
    booking_service: IBookingService = providers.Factory(BookingService)
    city_service: ICityService = providers.Factory(CityService)
    movie_service: IMovieService = providers.Factory(MovieService)
    seats_service: ISeatService  = providers.Factory(SeatService)
    register_service: IUserService = providers.Factory(UserService)
