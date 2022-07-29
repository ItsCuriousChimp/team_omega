from datetime import datetime
from django.db import connection
from abc import ABC, abstractmethod
from book_my_show.coreapis.dtos.cinema_dto import CinemaDto
from book_my_show.coreapis.models.cinema_model import Cinema
from book_my_show.coreapis.models.showtime_model import Showtime
from book_my_show.coreapis.serialisers.cinema_serialiser import (
    ShowtimeSerialiser,
)


class ICinemaRepository(ABC):
    @abstractmethod
    def get_cinemas_by_movie_id(self):
        raise NotImplementedError("Abstract method not implemented.")


class CinemaRepository(ICinemaRepository):
    def get_cinemas_by_movie_id(self, movie_id: str) -> dict[list[CinemaDto]]:
        test1 = Showtime.objects.filter(movie_id=movie_id)
        d = ShowtimeSerialiser(test1, many=True).data
        print(d)

        cursor = connection.cursor()
        cursor.execute(
            """Select s.id as showtime_id, s.start_time_at_utc, s.end_time_at_utc, 
                m.name as movie_name, c.name as cinema_name, c.id as cinema_id
                            From coreapis_ShowTime as s 
                            INNER JOIN coreapis_Movie as m
                                ON m.id = s.movie_id
                            INNER JOIN coreapis_CinemaScreen as sc 
                                ON s.cinema_screen_id = sc.id
                            INNER JOIN coreapis_Cinema as c
                                ON sc.cinema_id = c.id
                            WHERE s.movie_id= %s  
                            AND s.deleted IS NULL 
                            AND s.start_time_at_utc >= %s""",
            [movie_id, datetime.now()],
        )
        data: dict[list[CinemaDto]] = self.get_cinemas_grouped_by_id(cursor)
        return data

    def get_cinemas_grouped_by_id(self, cursor) -> dict[list[CinemaDto]]:
        list_cinemas: list[CinemaDto] = self.get_cinema_dtos_list(cursor)
        groupby_cinema: dict = {}

        for cinema in list_cinemas:
            if cinema.cinema_id in groupby_cinema:
                groupby_cinema[cinema.cinema_id].append(cinema)
            else:
                groupby_cinema[cinema.cinema_id] = [cinema]

        return groupby_cinema

    def get_cinema_dtos_list(self, cursor) -> list[CinemaDto]:

        columns = [col[0] for col in cursor.description]
        list_cinema = []

        for row in cursor.fetchall():
            cinema_dto_obj = CinemaDto(
                showtime_id=row[columns.index("showtime_id")],
                start_time_at_utc=row[columns.index("start_time_at_utc")],
                end_time_at_utc=row[columns.index("end_time_at_utc")],
                movie_name=row[columns.index("movie_name")],
                cinema_name=row[columns.index("cinema_name")],
                cinema_id=row[columns.index("cinema_id")],
            )
            list_cinema.append(cinema_dto_obj)

        return list_cinema
