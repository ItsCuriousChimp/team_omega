from abc import ABC
from book_my_show.coreapis.models.movie_model import Movie
from book_my_show.coreapis.repositories.movie_repository import IMovieRepository
from book_my_show.containers.repo_container import RepositoryContainer
from dependency_injector.wiring import inject, Provide


class IMovieService(ABC):
    def get_movies_list(self):
        pass


class MovieService(IMovieService):
    def __init__(
        self,
        movie_repository: IMovieRepository = Provide[
            RepositoryContainer.movie_repository
        ],
    ) -> None:
        self.movie_repository = movie_repository

    @inject
    def get_movies_list(
        self,
        city_pk: str,
    ) -> list[dict]:
        movies_in_city: Movie = self.movie_repository.get_movies_by_city_id(city_pk)
        movies_list = []

        for movie in movies_in_city:
            movie_detail = {}
            movie_detail["Movie_Id"] = str(movie.id)
            movie_detail["Movie_Name"] = str(movie)
            movies_list.append(movie_detail)

        return movies_list
