from book_my_show.coreapis.models.cinema_model import City
from abc import ABC, abstractmethod
from book_my_show.coreapis.dtos.city_model_dto import CityModelDto


class ICityRepository(ABC):
    @abstractmethod
    def get_city_list(self):
        raise NotImplementedError("Abstract method not implemented.")


class CityRepository(ICityRepository):
    def get_city_list(self) -> list[CityModelDto]:
        city_list: City = City.objects.all()
        city_dto_list: list[CityModelDto] = []

        for city in city_list:
            city_model_dto_obj: CityModelDto = CityModelDto(str(city), str(city.id))
            city_dto_list.append(city_model_dto_obj)

        return city_dto_list
