from book_my_show.coreapis.repositories.cinema_repository import CinemaRepository


class CinemaService:
    def get_cinemas(self, movie_pk: str) -> dict:
        cinema_repository = CinemaRepository()
        allcinemas_playing_movies = cinema_repository.get_cinemas(movie_pk)
        return allcinemas_playing_movies
