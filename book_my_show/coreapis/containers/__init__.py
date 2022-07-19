import imp
from django.conf import settings

# from book_my_show.coreapis.containers.repo_container import RepositoryContainer
from book_my_show.coreapis.containers.service_container import ServiceContainer

# from .service_container import ServiceContainer
from book_my_show.coreapis.containers.repo_container import RepositoryContainer


service_container = ServiceContainer()
repo_container = RepositoryContainer()
# container.config.from_dict(settings.__dict__)
