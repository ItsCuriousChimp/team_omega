from django.db import models
from book_my_show.coreapis.models.city_model import City


class Cinema(models.Model):
    name = models.CharField(max_length=32)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
