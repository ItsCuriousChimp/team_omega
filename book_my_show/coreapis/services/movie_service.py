from book_my_show.coreapis.repositories.movie_repository import MovieRepository
class MovieService:
    
    cinema_repository = MovieRepository()
    def get_movies_list(self, city_pk:str) -> list:
        
        movies_in_city = self.cinema_repository.get_cinemas(city_pk)
        movies_list = []
        for i in movies_in_city:
            movie_detail = {}
            movie_detail["Movie_Id"] = str(i.id)
            movie_detail["Movie_Name"] = str(i)
            movies_list.append(movie_detail)

        return movies_list