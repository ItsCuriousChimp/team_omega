from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from ..services.account_manager_service import MyAccountManagerService


class UserModel(AbstractBaseUser):
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

    objects = MyAccountManagerService()

    def __str__(self) -> str:
        return self.email

    def has_module_perms(self, app_label) -> bool:
        return True

    def has_perm(self, perm, obj=None) -> bool:
        return self.is_admin
