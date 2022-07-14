from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from book_my_show.authenticate.services.user_service import UserService
from django.db import connection


class AllTable(APIView):
    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        cursor.execute("Select * From coreapis_Cinema Where deleted IS NULL")
        cinemas = self.dictfetchall(cursor)
        cursor.execute("Select * From coreapis_Movie")
        movies = self.dictfetchall(cursor)
        cursor.execute("Select * From coreapis_ShowTime")
        showtime = self.dictfetchall(cursor)
        cursor.execute("Select * From coreapis_Booking")
        booking = self.dictfetchall(cursor)
        cursor.execute("Select * From coreapis_City")
        city = self.dictfetchall(cursor)
        cursor.execute("Select * From coreapis_CinemaScreen")
        cinema_screen = self.dictfetchall(cursor)
        cursor.execute("Select * From coreapis_Seat")
        seat = self.dictfetchall(cursor)
        return Response(
            {
                "cinemas": cinemas,
                "movies": movies,
                "showtimes": showtime,
                "cinema_screen": cinema_screen,
                "booking": booking,
                "city": city,
                "seat": seat,
            }
        )

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]