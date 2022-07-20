from abc import ABC
from book_my_show.coreapis.repositories.cinema_repository import ICinemaRepository
from dependency_injector.wiring import inject, Provide
from book_my_show.containers.repo_container import RepositoryContainer


class ICinemaService(ABC):
    def get_cinema(self):
        pass


class CinemaService:
    def __init__(
        self,
        cinema_repository: ICinemaRepository = Provide[
            RepositoryContainer.cinema_repository
        ],
    ) -> None:
        self.cinema_repository = cinema_repository

    @inject
    def get_cinemas(
        self,
        movie_pk: str,
    ) -> dict:
        allcinemas_playing_movies: dict = (
            self.cinema_repository.get_cinemas_by_movie_id(movie_pk)
        )

        return allcinemas_playing_movies
