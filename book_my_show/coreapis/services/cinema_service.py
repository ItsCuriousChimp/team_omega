from book_my_show.coreapis.repositories.cinema_repository import CinemaRepository


class CinemaService:
    cinema_repository = CinemaRepository()

    def get_cinemas(self, movie_pk: str) -> dict:

        allcinemas_playing_movies = self.cinema_repository.get_cinemas(movie_pk)
        return allcinemas_playing_movies
