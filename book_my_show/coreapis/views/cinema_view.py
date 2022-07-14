from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from book_my_show.authenticate.services.user_service import UserService
from django.db import connection

from book_my_show.coreapis.services.cinema_service import CinemaService


class CinemaView(APIView):
    def get(self, request, *args, **kwargs):
        movie_pk = self.kwargs["pk1"]
        cinema_service = CinemaService()
        allcinemas_playing_movies = cinema_service.get_cinemas(movie_pk)
        return Response(allcinemas_playing_movies)
