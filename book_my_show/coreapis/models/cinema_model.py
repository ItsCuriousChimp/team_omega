from django.db import models
from book_my_show.coreapis.models.city_model import City
from book_my_show.common.models.base_model import BaseModel


class Cinema(BaseModel):
    name = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)

    def delete(self):
        print("updating cinemas")
        Cinema.objects.update(is_deleted=True)
