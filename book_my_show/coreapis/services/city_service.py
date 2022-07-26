from abc import ABC, abstractmethod
from book_my_show.coreapis.repositories.city_repository import ICityRepository
from book_my_show.containers.repo_container import RepositoryContainer
from dependency_injector.wiring import Provide

from book_my_show.coreapis.dtos.city_model_dto import CityModelDto


class ICityService(ABC):
    @abstractmethod
    def fetch_city_list(self):
        raise NotImplementedError("Abstract method not implemented.")

class CityService(ICityService):
    def __init__(
        self,
        city_repository: ICityRepository = Provide[RepositoryContainer.city_repository],
    ) -> None:
        self.city_repository = city_repository

    def fetch_city_list(
        self,
    ) -> list[CityModelDto]:
        city_dto_list: list[CityModelDto] = self.city_repository.get_city_list()

        return city_dto_list
