from book_my_show.coreapis.repositories.movie_repository import MovieRepository
class MovieService:
    cinema_repository = MovieRepository()
    def get_movies_list(self, city_pk) -> list:
        
        movies_in_city = self.cinema_repository.get_cinemas(city_pk)
        ls = {}
        for i in movies_in_city:
            ls[str(i.movie_id.id)] = str(i.movie_id)
        return ls
    # def get_city_name(self, city_pk) ->str:
    #     return str(self.cinema_repository.get_city_name(city_pk))