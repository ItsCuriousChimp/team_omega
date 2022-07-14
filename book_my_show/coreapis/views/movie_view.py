import json
from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.movie_service import MovieService

class MovieList(APIView):
    # GET /v1/coreapis/city/<str:id>/movies
    movie_service = MovieService()
    def get(self, request, id: str) -> JsonResponse:
        city_pk = id
        
        ls = self.movie_service.get_movies_list(city_pk)
        json.dumps(ls)
        var1 = json.dumps(ls, indent=2)
        return JsonResponse(
            ls, 
            safe = False
        )

