from book_my_show.coreapis.models.cinema_model import City
class CityRepository:


    def get_city_list(self) -> City:
        city_list = City.objects.all()
        
        return city_list
