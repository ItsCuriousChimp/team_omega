from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.containers.service_container import ServiceContainer
from dependency_injector.wiring import inject, Provide
from book_my_show.coreapis.services.cinema_service import ICinemaService


class CinemaView(APIView):
    # GET /v1/movies/<str:id>/cinemas/
    def __init__(
        self,
        cinema_service: ICinemaService = Provide[ServiceContainer.cinema_service],
    ) -> None:
        self.cinema_service = cinema_service

    def get(
        self,
        request,
        id: str,
    ) -> JsonResponse:
        movie_pk = id
        allcinemas_playing_movies = self.cinema_service.get_cinemas(movie_pk)

        return JsonResponse(allcinemas_playing_movies)
