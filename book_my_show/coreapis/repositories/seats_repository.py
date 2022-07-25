from django.db import connection
from abc import ABC, abstractmethod


class ISeatRepository(ABC):
    @abstractmethod
    def get_all_seats_by_show_time_id(self):
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def get_unavailable_seats_by_show_time_id(self):
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def get_available_seats_by_show_time_id(self):
        raise NotImplementedError("Abstract method not implemented.")


class SeatRepository(ISeatRepository):
    def get_all_seats_by_show_time_id(self, showtime_id: str) -> list[dict]:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT s.id as seat_id, s.seat_no as seat_number
                FROM coreapis_Seat as s
                INNER JOIN coreapis_CinemaScreen as cs
                    ON s.cinema_screen_id = cs.id
                INNER JOIN coreapis_Showtime as sh
                    ON cs.id = sh.cinema_screen_id
                WHERE sh.id = %s
                AND sh.deleted IS NULL 
                AND s.deleted IS NULL
            """,
            (showtime_id,),
        )
        data = self.dictfetchall(cursor)
        return data

    def get_unavailable_seats_by_show_time_id(self, showtime_id: str) -> list[dict]:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT s.id as seat_id, s.seat_no as seat_number, 'unavailable' as availability
                FROM coreapis_Seat as s
                INNER JOIN coreapis_Booking as b
                    ON s.id = b.seat_id
                WHERE b.show_time_id = %s
                AND b.deleted IS NULL
            """,
            (showtime_id,),
        )
        data = self.dictfetchall(cursor)
        return data

    def get_available_seats_by_show_time_id(self, showtime_id: str) -> list[dict]:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT s.id as seat_id, s.seat_no as seat_number, 'available' as availability
                FROM coreapis_Seat as s
                INNER JOIN coreapis_CinemaScreen as cs
                    ON s.cinema_screen_id = cs.id
                INNER JOIN coreapis_Showtime as sh
                    ON cs.id = sh.cinema_screen_id
                WHERE sh.id = %s
                AND s.id NOT IN (
                    SELECT b.seat_id
                    FROM coreapis_Booking as b
                    INNER JOIN coreapis_Showtime as sh
                        ON b.show_time_id = %s
                    AND b.deleted is NULL
                )
                AND sh.deleted IS NULL 
                AND s.deleted IS NULL
            """,
            (
                showtime_id,
                showtime_id,
            ),
        )
        data = self.dictfetchall(cursor)
        return data

    def dictfetchall(self, cursor) -> list[dict]:
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
