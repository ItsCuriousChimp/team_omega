from abc import ABC, abstractmethod
from book_my_show.coreapis.models.city_model import City
from book_my_show.coreapis.repositories.city_repository import ICityRepository
from book_my_show.containers.repo_container import RepositoryContainer
from dependency_injector.wiring import Provide


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
    ) -> list[dict]:
        city_list: City = self.city_repository.get_city_list()
        cities_details = []

        for city in city_list:
            detail = {}
            detail["id"] = str(city.id)
            detail["City_Name"] = str(city)
            cities_details.append(detail)

        return cities_details
