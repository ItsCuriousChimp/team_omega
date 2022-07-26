from django.http import JsonResponse
from rest_framework.views import APIView
from dependency_injector.wiring import Provide
from book_my_show.containers.service_container import ServiceContainer
from book_my_show.coreapis.services.movie_service import IMovieService
from book_my_show.coreapis.dtos.movie_model_dto import MovieModelDto


class MovieList(APIView):
    def __init__(
        self,
        movie_service: IMovieService = Provide[ServiceContainer.movie_service],
    ) -> None:
        self.movie_service = movie_service

    # GET /v1/cities/<str:id>/movies/
    def get(
        self,
        request,
        id: str,
    ) -> JsonResponse:
        movies_list: MovieModelDto = self.movie_service.get_movies_list(id)
        movies_details_list: list[dict] = []
        for movie in movies_list:
            movie_details = {}
            movie_details["Name"] = movie.name
            movie_details["Id"] = movie.id
            movies_details_list.append(movie_details)

        return JsonResponse(
            movies_details_list, 
            safe=False
            )
