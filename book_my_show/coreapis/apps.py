from django.apps import AppConfig

from book_my_show.coreapis.containers import container


class CoreapisConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "book_my_show.coreapis"
