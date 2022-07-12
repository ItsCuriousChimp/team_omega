from django.db import models


class BaseModel(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
