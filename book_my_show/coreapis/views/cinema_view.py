from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.containers import Services
from book_my_show.coreapis.services.cinema_service import CinemaService
from dependency_injector.wiring import inject, Provide


class CinemaView(APIView):

    # GET /v1/movies/<str:id>/cinemas/
    @inject
    def get(
        self,
        request,
        id: str,
        cinema_service: CinemaService = Provide[Services.cinema_service],
    ) -> JsonResponse:
        movie_pk = id
        print(type(cinema_service))
        allcinemas_playing_movies = cinema_service.get_cinemas(movie_pk)

        return JsonResponse(allcinemas_playing_movies)
