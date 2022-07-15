from book_my_show.coreapis.models.city_model import City
from book_my_show.coreapis.repositories.city_repository import CityRepository


class CityService:
    city_repository = CityRepository()

    def fetch_city_list(self) -> list[dict]:
        city_list: City = self.city_repository.get_city_list()
        cities_details = []

        for city in city_list:
            detail = {}
            detail["id"] = str(city.id)
            detail["City_Name"] = str(city)
            cities_details.append(detail)

        return cities_details
