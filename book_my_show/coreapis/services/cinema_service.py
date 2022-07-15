from book_my_show.coreapis.repositories.cinema_repository import CinemaRepository


class CinemaService:
    cinema_repository = CinemaRepository()

    def get_cinemas(self, movie_pk: str) -> dict:

        allcinemas_playing_movies: dict = (
            self.cinema_repository.get_cinemas_by_movie_id(movie_pk)
        )
        return allcinemas_playing_movies
