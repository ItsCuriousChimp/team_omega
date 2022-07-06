from book_my_show.config.settings import Settings


class Local(Settings):
    DEBUG = True
    ALLOWED_HOSTS = []