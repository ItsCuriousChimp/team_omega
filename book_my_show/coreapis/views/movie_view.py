from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.movie_service import MovieService
from dependency_injector.wiring import inject, Provide
from book_my_show.containers import Services


class MovieList(APIView):

    # GET /v1/cities/<str:id>/movies/
    @inject
    def get(
        self,
        request,
        id: str,
        movie_service: MovieService = Provide[Services.movie_service],
    ) -> JsonResponse:

        movies_list = movie_service.get_movies_list(id)

        return JsonResponse(movies_list, safe=False)
