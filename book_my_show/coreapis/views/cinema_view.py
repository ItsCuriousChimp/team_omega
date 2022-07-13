from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from book_my_show.authenticate.services.user_service import UserService
from django.db import connection


class CinemaView(APIView):
    def get(self, request, *args, **kwargs):
        movie_pk = self.kwargs["pk1"]
        cursor = connection.cursor()
        cursor.execute(
            """Select showtime.* ,movie.name as movie_name,cinema.name as cinema_name 
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
        return Response(data)

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


# SELECT TableA.*, TableB.*, TableC.*, TableD.*
# FROM TableA
#     JOIN TableB
#         ON TableB.aID = TableA.aID
#     JOIN TableC
#         ON TableC.cID = TableB.cID
#     JOIN TableD
#         ON TableD.dID = TableA.dID
# WHERE DATE(TableC.date)=date(now())

#  "SELECT * FROM coreapis_Cinema as cinema WHERE cinema.city_id_id = %s AND cinema.deleted IS NULL",
#             [pk],
