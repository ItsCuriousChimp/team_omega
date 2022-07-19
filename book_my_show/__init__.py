import django

django.setup()

from book_my_show.containers.service_container import ServiceContainer

from book_my_show.containers.repo_container import RepositoryContainer

service_container = ServiceContainer()
repo_container = RepositoryContainer()
