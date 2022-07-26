from book_my_show.coreapis.models.cinema_model import City
from abc import ABC, abstractmethod


class ICityRepository(ABC):
    @abstractmethod
    def get_city_list(self):
        raise NotImplementedError("Abstract method not implemented.")


class CityRepository(ICityRepository):
    def get_city_list(self) -> City:
        city_list = City.objects.filter(is_deleted=False)
        print(city_list)

        return city_list
