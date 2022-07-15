from book_my_show.coreapis.models.city_model import City
from book_my_show.coreapis.models.movie_model import Movie


class MovieRepository:
    def get_movies_by_city_id(self, city_pk: str) -> Movie:

        movie_model = Movie.objects.all().filter(cinema_id__city_id_id=int(city_pk))

        return movie_model
