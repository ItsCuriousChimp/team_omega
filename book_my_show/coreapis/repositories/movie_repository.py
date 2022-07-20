from book_my_show.coreapis.models.movie_model import Movie
from abc import ABC, abstractmethod


class IMovieRepository(ABC):
    @abstractmethod
    def get_movies_by_city_id(self):
        pass


class MovieRepository(IMovieRepository):
    def get_movies_by_city_id(self, city_pk: str) -> Movie:

        movie_model = Movie.objects.all().filter(cinema_id__city_id_id=int(city_pk))

        return movie_model
