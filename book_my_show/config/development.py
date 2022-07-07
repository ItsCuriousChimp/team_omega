from book_my_show.config.settings import Settings
from book_my_show.common.enums.app_environment import AppEnvironment


class Development(Settings):
    APP_ENVIRONMENT = AppEnvironment.Development
