from django.db import models
from book_my_show.coreapis.models.cinema_screen_model import CinemaScreen
from book_my_show.coreapis.models.movie_model import Movie
from book_my_show.common.models.base_model import BaseModel
from softdelete.models import SoftDeleteObject


class Showtime(BaseModel, SoftDeleteObject):
    start_time_at_utc = models.DateTimeField()
    end_time_at_utc = models.DateTimeField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_screen_id = models.ForeignKey(CinemaScreen, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(str(self.movie_id) + " " + str(self.cinema_screen_id))

    # def clean(self) -> None:

    #     self.check_clash()

    #     print("its running", self.cinema_screen_id)

    # def check_clash(self):
    #     queryset = self._meta.default_manager.filter(
    #         cinema_screen_id=self.cinema_screen_id
    #     )
    #     print("start Time ", queryset[0].start_time_at_utc)
    #     movies = queryset.filter(
    #         (
    #             start_time_at_utc < self.start_time_at_utc
    #             and end_time_at_utc < self.end_time_at_utc
    #         )
    #         or start_time_at_utc > self.start_time_at_utc
    #         and end_time_at_utc > self.end_time_at_utc
    #     )
    # print("First ", queryset)
    # print("Second ", movies)
