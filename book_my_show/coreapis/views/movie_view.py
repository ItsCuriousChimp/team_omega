from django.http import JsonResponse
from rest_framework.views import APIView
from dependency_injector.wiring import inject, Provide
from book_my_show.containers.service_container import ServiceContainer
from book_my_show.coreapis.services.movie_service import IMovieService


class MovieList(APIView):
    # GET /v1/cities/<str:id>/movies/
    def __init__(
        self,
        movie_service: IMovieService = Provide[ServiceContainer.movie_service],
    ) -> None:
        self.movie_service = movie_service

    @inject
    def get(
        self,
        request,
        id: str,
    ) -> JsonResponse:
        movies_list = self.movie_service.get_movies_list(id)

        return JsonResponse(movies_list, safe=False)
