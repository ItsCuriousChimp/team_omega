from abc import ABC, abstractmethod
from book_my_show.coreapis.repositories.cinema_repository import ICinemaRepository
from dependency_injector.wiring import Provide
from book_my_show.containers.repo_container import RepositoryContainer


class ICinemaService(ABC):
    @abstractmethod
    def get_cinema(self):
        raise NotImplementedError("Abstract method not implemented.")


class CinemaService(ICinemaService):
    def __init__(
        self,
        cinema_repository: ICinemaRepository = Provide[
            RepositoryContainer.cinema_repository
        ],
    ) -> None:
        self.cinema_repository = cinema_repository

    def get_cinemas(
        self,
        movie_id: str,
    ) -> dict:
        allcinemas_playing_movies: dict = (
            self.cinema_repository.get_cinemas_by_movie_id(movie_id)
        )

        return allcinemas_playing_movies
