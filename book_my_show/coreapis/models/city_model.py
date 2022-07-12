from django.db import models
from book_my_show.common.models.base_model import BaseModel
from softdelete.models import SoftDeleteObject


class City(BaseModel, SoftDeleteObject):
    name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.name)
