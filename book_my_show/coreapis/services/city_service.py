from book_my_show.coreapis.models.city_model import City
from book_my_show.coreapis.repositories.city_repository import CityRepository
class CityService:

    
    city_repository = CityRepository()
    def fetch_city_list(self) -> list:
        city_list = self.city_repository.get_city_list()
        
        city_list_dict = []

        for i in city_list:
            temp_list = {}
            temp_list["id"] = str(i.id)
            temp_list["City_Name"] = str(i)
            city_list_dict.append(temp_list)
        return city_list_dict