from django.http import JsonResponse
from rest_framework.views import APIView

from book_my_show.coreapis.services.cinema_service import CinemaService


class CinemaView(APIView):
    # GET /v1/movies/<str:id>/cinema/
    def get(self, request, id):
        movie_pk = id
        cinema_service = CinemaService()
        allcinemas_playing_movies = cinema_service.get_cinemas(movie_pk)

        return JsonResponse({"cinema_playing_movies": allcinemas_playing_movies})
