from datetime import datetime
from django.db import connection


class CinemaRepository:
    def get_cinemas_by_movie_id(self, movie_pk: str) -> dict:
        cursor = connection.cursor()
        cursor.execute(
            """Select s.id as showtime_id, s.start_time_at_utc, s.end_time_at_utc, 
                m.name as movie_name, c.name as cinema_name, c.id as cinema_id
                            From coreapis_ShowTime as s 
                            INNER JOIN coreapis_Movie as m
                                ON m.id = s.movie_id_id
                            INNER JOIN coreapis_CinemaScreen as sc 
                                ON s.cinema_screen_id_id = sc.id
                            INNER JOIN coreapis_Cinema as c
                                ON sc.cinema_id_id = c.id
                            WHERE s.movie_id_id= %s  AND s.deleted IS NULL AND s.start_time_at_utc >= %s""",
            [movie_pk, datetime.now()],
        )
        data: dict = self.dictfetchall(cursor)
        return data

    def dictfetchall(self, cursor) -> dict:
        columns = [col[0] for col in cursor.description]
        dict_cinema = [dict(zip(columns, row)) for row in cursor.fetchall()]

        groupby_cinema: dict = {}

        for cinema in dict_cinema:
            if cinema["cinema_id"] in groupby_cinema:
                groupby_cinema[cinema["cinema_id"]].append(cinema)

            else:
                groupby_cinema[cinema["cinema_id"]] = [cinema]

        return groupby_cinema
