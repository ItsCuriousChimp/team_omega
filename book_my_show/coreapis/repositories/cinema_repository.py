from django.db import connection


class CinemaRepository:
    def get_cinemas(self, movie_pk):
        cursor = connection.cursor()
        cursor.execute(
            """Select showtime.start_time_at_utc,showtime.end_time_at_utc ,movie.name as movie_name,cinema.name as cinema_name 
                            From coreapis_ShowTime as showtime 
                            JOIN coreapis_Movie as movie
                                ON movie.id == showtime.movie_id_id
                            JOIN coreapis_CinemaScreen as screen 
                                ON showtime.cinema_screen_id_id == screen.id
                            JOIN coreapis_Cinema as cinema
                                ON screen.cinema_id_id == cinema.id
                            WHERE showtime.movie_id_id= %s  AND showtime.deleted IS NULL""",
            [movie_pk],
        )
        data = self.dictfetchall(cursor)
        return data

    def dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
