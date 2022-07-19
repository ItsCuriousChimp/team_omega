from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.containers.container import Container
from book_my_show.coreapis.services.cinema_service import CinemaService
from dependency_injector.wiring import inject, Provide


class CinemaView(APIView):
    # cinema_service = CinemaService()

    # GET /v1/movies/<str:id>/cinemas/
    @inject
    def get(
        self,
        request,
        id: str,
        cinema_service: CinemaService = Provide[Container.service],
    ) -> JsonResponse:
        movie_pk = id
        allcinemas_playing_movies = cinema_service.get_cinemas(movie_pk)

        return JsonResponse(allcinemas_playing_movies)
