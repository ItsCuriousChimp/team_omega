from abc import ABC, abstractmethod
from book_my_show.coreapis.models.movie_model import Movie
from book_my_show.coreapis.repositories.movie_repository import IMovieRepository
from book_my_show.containers.repo_container import RepositoryContainer
from dependency_injector.wiring import Provide

from book_my_show.coreapis.dtos.movie_model_dto import MovieModelDto


class IMovieService(ABC):
    @abstractmethod
    def get_movies_list(self):
        raise NotImplementedError("Abstract method not implemented.")


class MovieService(IMovieService):
    def __init__(
        self,
        movie_repository: IMovieRepository = Provide[
            RepositoryContainer.movie_repository
        ],
    ) -> None:
        self.movie_repository = movie_repository

    def get_movies_list(
        self,
        city_id: str,
    ) -> list[dict]:
        movies_in_city: MovieModelDto = self.movie_repository.get_movies_by_city_id(city_id)

        return movies_in_city
