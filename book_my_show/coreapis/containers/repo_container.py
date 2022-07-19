from dependency_injector import containers, providers
from book_my_show.coreapis.repositories.cinema_repository import CinemaRepository


class RepositoryContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "book_my_show.coreapis.services.cinema_service",
        ],
    )
    # config = providers.Configuration()

    cinema_repo = providers.Factory(CinemaRepository)
