import json
from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.models.cinema_model import City
from book_my_show.coreapis.services.city_service import CityService
class CityView(APIView):

    city_service = CityService()
    def get(self, request) -> JsonResponse:
        
        city_list = self.city_service.fetch_city_list()

        
        return JsonResponse(city_list, safe=False)

