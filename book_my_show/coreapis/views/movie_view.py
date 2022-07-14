from tkinter import E
from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.models.city_model import City
from book_my_show.coreapis.models.showtime_model import Showtime

class MovieList(APIView):

    def get(self, request,*args, **kwargs):
        movie_pk = self.kwargs["pk1"]
        movie_in_city = Showtime.objects.filter(cinema_screen_id__cinema_id_id__city_id_id__id= int(movie_pk))
        city = City.objects.all().filter(id = int(movie_pk))
        
        ls = []
        
        for i in movie_in_city:
            ls.append(str(i.movie_id))
        city_name = "NULL"
        if city:
            city_name = str(city[0])

        return JsonResponse(
           { city_name: ls}
        )

