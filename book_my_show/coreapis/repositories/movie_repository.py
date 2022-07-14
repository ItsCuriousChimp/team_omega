
from book_my_show.coreapis.models.city_model import City
from book_my_show.coreapis.models.showtime_model import Showtime


class MovieRepository:
    def get_cinemas(self, city_pk: str) ->Showtime:
        movie_in_city = Showtime.objects.filter(cinema_screen_id__cinema_id_id__city_id_id__id= int(city_pk))
        return movie_in_city

