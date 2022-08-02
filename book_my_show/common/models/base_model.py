from statistics import mode
from django.db import models

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


# class BaseModelManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_deleted=False)


# class BaseModel(models.Model):

#     is_deleted = models.BooleanField(default=False)
#     created_at_utc = models.DateTimeField(auto_now_add=True)
#     modified_at_utc = models.DateTimeField(auto_now=True)
#     # objects = BaseModelManager()
#     all_objects = models.Manager()

#     def delete(self):
#         f = self._meta.get_fields()
#         if f.is_relation:
#             print(f)
#         print("deleting")
#         self.is_deleted = True
#         self.save()

#     def restore(self):
#         self.is_deleted = False
#         self.save()

#     class Meta:
#         abstract = True


class BaseModel(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
