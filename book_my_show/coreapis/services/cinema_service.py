from book_my_show.coreapis.repositories.cinema_repository import CinemaRepository
from abc  import ABC
from dependency_injector.wiring import Provide
from book_my_show.containers.repo_container import RepositoryContainer

class ICinemaService(ABC):
    def get_cinema(self):
        pass

class CinemaService(ICinemaService):
    def get_cinemas(
        self,
        movie_pk: str,
        cinema_repository: CinemaRepository = Provide[
            RepositoryContainer.cinema_repository
        ],
    ) -> dict:
        allcinemas_playing_movies: dict = cinema_repository.get_cinemas_by_movie_id(
            movie_pk
        )

        return allcinemas_playing_movies
