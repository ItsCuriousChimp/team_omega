from book_my_show.coreapis.repositories.movie_repository import MovieRepository
class MovieService:
    def get_movies(self, city_pk):
        cinema_repository = MovieRepository()
        movies_in_city = cinema_repository.get_cinemas(city_pk)
        ls = []
        for i in movies_in_city:
            ls.append(str(i.movie_id))
        return ls
    def get_city_name(self, city_pk):
        cinema_repository = MovieRepository()
        return str(cinema_repository.get_city_name(city_pk))