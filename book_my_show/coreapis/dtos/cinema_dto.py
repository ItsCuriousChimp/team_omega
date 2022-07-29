from datetime import datetime


class CinemaDto:
    def __init__(
        self,
        showtime_id: str,
        start_time_at_utc: datetime,
        end_time_at_utc: datetime,
        movie_name: str,
        cinema_name: str,
        cinema_id: str,
    ) -> None:
        self.showtime_id = showtime_id
        self.start_time_at_utc = start_time_at_utc
        self.end_time_at_utc = end_time_at_utc
        self.movie_name = movie_name
        self.cinema_name = cinema_name
        self.cinema_id = cinema_id
