from book_my_show.coreapis.models.cinema_model import City
from abc import ABC, abstractmethod  # Built in. No install needed.


class ICityRepository(ABC):
    @abstractmethod
    def get_city_list(self):
        pass


class CityRepository(ICityRepository):
    def get_city_list(self) -> City:
        city_list = City.objects.all()

        return city_list
