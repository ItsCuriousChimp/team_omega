from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from ..services.user_manager_service import UserManagerService
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from safedelete.models import SafeDeleteModel


class UserModel(SafeDeleteModel, AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email", max_length=60, unique=True, primary_key=True
    )
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    phone_no = models.CharField(max_length=15, null=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManagerService()

    def __str__(self) -> str:
        return self.email

    def has_module_perms(self, app_label) -> bool:
        return True

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_admin


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs) -> None:
    if created:
        Token.objects.create(user=instance)
