from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

class BaseModel(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
