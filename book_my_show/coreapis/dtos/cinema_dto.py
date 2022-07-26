class CinemaDto:
    def __init__(
        self,
        showtime_id,
        start_time_at_utc,
        end_time_at_utc,
        movie_name,
        cinema_name,
        cinema_id,
    ) -> None:
        self.showtime_id = showtime_id
        self.start_time_at_utc = start_time_at_utc
        self.end_time_at_utc = end_time_at_utc
        self.movie_name = movie_name
        self.cinema_name = cinema_name
        self.cinema_id = cinema_id
