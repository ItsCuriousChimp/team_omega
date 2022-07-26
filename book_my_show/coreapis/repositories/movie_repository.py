from book_my_show.coreapis.models.movie_model import Movie
from abc import ABC, abstractmethod

from book_my_show.coreapis.dtos.movie_model_dto import MovieModelDto


class IMovieRepository(ABC):
    @abstractmethod
    def get_movies_by_city_id(self):
        raise NotImplementedError("Abstract method not implemented.")


class MovieRepository(IMovieRepository):
    def get_movies_by_city_id(self, city_id: str) -> MovieModelDto:
        movie_model: Movie = Movie.objects.all().filter(cinema__city_id=int(city_id)).distinct()
        movies_dto_list: list[MovieModelDto] = []
        for movie in movie_model:
            movie_detail: MovieModelDto = MovieModelDto(str(movie.id), str(movie))
            movies_dto_list.append(movie_detail)
        return movies_dto_list
