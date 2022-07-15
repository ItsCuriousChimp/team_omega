from django.db import models
from book_my_show.common.models.base_model import BaseModel
from book_my_show.coreapis.models.cinema_model import Cinema


class Movie(BaseModel):
    name = models.CharField(max_length=32)
    description = models.TextField()
    release_date = models.DateField()
    cinema_id = models.ManyToManyField(Cinema)

    def __str__(self) -> str:
        return str(self.name)
