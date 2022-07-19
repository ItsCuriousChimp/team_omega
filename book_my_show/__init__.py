import django


django.setup()
from book_my_show.containers import Services

from book_my_show.repo_container import RepositoryContainer

service_container = Services()
repo_container = RepositoryContainer()
