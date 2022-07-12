from django.db import models
from book_my_show.common.models.base_model import BaseModel
from softdelete.models import SoftDeleteObject


class Movie(BaseModel, SoftDeleteObject):
    name = models.CharField(max_length=32)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return str(self.name)
