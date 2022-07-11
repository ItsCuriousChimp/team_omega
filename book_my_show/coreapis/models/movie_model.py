from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return str(self.name)
