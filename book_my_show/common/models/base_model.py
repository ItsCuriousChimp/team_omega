from django.db import models


class BaseModel(models.Model):
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
