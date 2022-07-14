from django.db import connection


class SeatAvailableRepository:
    def get_seat_available(self, showtime_pk: str):
        cursor = connection.cursor()
        cursor.execute(
            """SELECT s.id as seat_id, s.seat_no as seat_number
                FROM coreapis_Seat as s
                INNER JOIN coreapis_CinemaScreen as cs
                    ON s.cinema_screen_id_id == cs.id
                INNER JOIN coreapis_Showtime as sh
                    ON cs.id == sh.cinema_screen_id_id
                WHERE sh.id == %s
                AND s.id NOT IN (
                    SELECT b.seat_id_id
                    FROM coreapis_Booking as b
                    INNER JOIN coreapis_Showtime as sh
                        ON b.show_time_id_id == %s
                )
                AND sh.deleted IS NULL 
                AND s.deleted IS NULL
            """,
            (
                showtime_pk,
                showtime_pk,
            ),
        )
        data = self.dictfetchall(cursor)
        return data

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
