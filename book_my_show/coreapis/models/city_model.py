from django.db import models
from book_my_show.common.models.base_model import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return str(self.name)

    def delete(self):
        # print(self.)
        print(self.name)
        self.update(is_deleted=True)
