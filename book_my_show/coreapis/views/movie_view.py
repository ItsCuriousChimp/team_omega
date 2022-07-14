import json
from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.movie_service import MovieService

class MovieList(APIView):
    movie_service = MovieService()
    def get(self, request,*args, **kwargs) -> JsonResponse:
        city_pk = self.kwargs["pk1"]
        
        ls = self.movie_service.get_movies_list(city_pk)
        json.dumps()
        # city_name = self.movie_service.get_city_name(city_pk)
        return JsonResponse(
           { ls}
        )

