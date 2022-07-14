import json
from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.movie_service import MovieService

class MovieList(APIView):
    
    # GET /v1/coreapis/city/<str:id>/movies
    movie_service = MovieService()
    def get(self, request, id: str) -> JsonResponse:

        movies_list = self.movie_service.get_movies_list(id)

        return JsonResponse(
            movies_list, 
            safe = False
        )

