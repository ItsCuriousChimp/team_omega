from book_my_show.coreapis.models.movie_model import Movie
from abc import ABC, abstractmethod


class IMovieRepository(ABC):
    @abstractmethod
    def get_movies_by_city_id(self):
        raise NotImplementedError("Abstract method not implemented.")


class MovieRepository(IMovieRepository):
    def get_movies_by_city_id(self, city_id: str) -> Movie:

        movie_model = (
            Movie.objects.all().filter(cinema__city_id=int(city_id)).distinct()
        )

        return movie_model
