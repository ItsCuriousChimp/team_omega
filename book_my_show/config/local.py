from book_my_show.config.settings import Settings
from book_my_show.common.enums.app_environment import AppEnvironment


class Local(Settings):
    DEBUG = True
    ALLOWED_HOSTS = []
    APP_ENVIRONMENT = AppEnvironment.Local
