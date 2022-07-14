from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.cinema_service import CinemaService


class CinemaView(APIView):
    # GET /v1/movies/<str:id>/cinema/
    cinema_service = CinemaService()

    def get(self, request, id: str) -> JsonResponse:
        movie_pk = id
        allcinemas_playing_movies = self.cinema_service.get_cinemas(movie_pk)

        return JsonResponse(allcinemas_playing_movies)
