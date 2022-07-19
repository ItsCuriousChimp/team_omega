from book_my_show.coreapis.repositories.cinema_repository import CinemaRepository
from book_my_show.coreapis.containers.repo_container import RepositoryContainer
from dependency_injector.wiring import inject, Provide


class CinemaService:
    # cinema_repository = CinemaRepository()

    @inject
    def get_cinemas(
        self,
        movie_pk: str,
        cinema_repository: CinemaRepository = Provide[RepositoryContainer.cinema_repo],
    ) -> dict:
        allcinemas_playing_movies: dict = cinema_repository.get_cinemas_by_movie_id(
            movie_pk
        )

        return allcinemas_playing_movies
