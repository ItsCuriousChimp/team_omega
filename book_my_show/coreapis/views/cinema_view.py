from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.containers.service_container import ServiceContainer
from book_my_show.coreapis.services.cinema_service import CinemaService
from dependency_injector.wiring import inject, Provide
from book_my_show.coreapis.services.cinema_service import ICinemaService

class CinemaView(APIView):

    # GET /v1/movies/<str:id>/cinemas/
    @inject
    def get(
        self,
        request,
        id: str,
        cinema_service: ICinemaService = Provide[ServiceContainer.cinema_service],
    ) -> JsonResponse:
        movie_pk = id
        print(type(cinema_service))
        allcinemas_playing_movies = cinema_service.get_cinemas(movie_pk)

        return JsonResponse(allcinemas_playing_movies)
