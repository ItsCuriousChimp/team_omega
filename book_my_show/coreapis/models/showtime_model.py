from django.db import models
from book_my_show.coreapis.models.cinema_screen_model import CinemaScreen
from book_my_show.coreapis.models.movie_model import Movie
from book_my_show.common.models.base_model import BaseModel


class Showtime(BaseModel):
    start_time_at_utc = models.DateTimeField()
    end_time_at_utc = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_screen = models.ForeignKey(CinemaScreen, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(str(self.movie) + " " + str(self.cinema_screen))
