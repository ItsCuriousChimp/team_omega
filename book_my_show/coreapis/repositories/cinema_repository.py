from django.db import connection


class CinemaRepository:
    def get_cinemas(self, movie_pk: str) -> dict:
        cursor = connection.cursor()
        cursor.execute(
            """Select show.id as showtime_id,show.start_time_at_utc,show.end_time_at_utc ,m.name as movie_name,c.name as cinema_name ,c.id as cinema_id,show.movie_id_id as movie_id
                            From coreapis_ShowTime as show 
                            INNER JOIN coreapis_Movie as m
                                ON m.id == show.movie_id_id
                            INNER JOIN coreapis_CinemaScreen as sc 
                                ON show.cinema_screen_id_id == sc.id
                            INNER JOIN coreapis_Cinema as c
                                ON sc.cinema_id_id == c.id
                            WHERE show.movie_id_id= %s  AND show.deleted IS NULL """,
            [movie_pk],
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
