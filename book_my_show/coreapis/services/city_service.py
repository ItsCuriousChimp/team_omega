from book_my_show.coreapis.models.city_model import City
from book_my_show.coreapis.repositories.city_repository import CityRepository
from book_my_show.repo_container import RepositoryContainer
from dependency_injector.wiring import inject, Provide


class CityService:
    city_repository = CityRepository()

    @inject
    def fetch_city_list(
        self,
        city_repository: CityRepository = Provide[RepositoryContainer.city_repository],
    ) -> list[dict]:
        city_list: City = city_repository.get_city_list()
        cities_details = []

        for city in city_list:
            detail = {}
            detail["id"] = str(city.id)
            detail["City_Name"] = str(city)
            cities_details.append(detail)

        return cities_details
