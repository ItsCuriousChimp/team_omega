from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.movie_service import MovieService

class MovieList(APIView):

    def get(self, request,*args, **kwargs):
        movie_pk = self.kwargs["pk1"]
        movie_service = MovieService()
        ls = movie_service.get_movies(movie_pk)
        city_name = movie_service.get_city_name(movie_pk)
        return JsonResponse(
           { city_name: ls}
        )

