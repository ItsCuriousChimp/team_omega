from rest_framework.views import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from book_my_show.authenticate.services.user_service import UserService
from django.db import connection
from book_my_show.coreapis.models.showtime_model import Showtime


class MovieInCity(APIView):
    def get(self, request, *args, **kwargs):
        movie_pk = self.kwargs["pk"]
        obj = Showtime.objects.filter(cinema_screen_id__cinema_id_id__city_id_id__id=2)
        print(obj)
        data = Showtime.objects.all()

        return Response("hi")
