from django.db import models
from book_my_show.coreapis.models.cinema_screen_model import CinemaScreen
from book_my_show.coreapis.models.movie_model import Movie


class Showtime(models.Model):
    start_time_at_utc = models.DateTimeField()
    end_time_at_utc = models.DateTimeField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_screen_id = models.ForeignKey(CinemaScreen, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(str(self.movie_id) + " " + str(self.cinema_screen_id))
