from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.city_service import CityService


class CityView(APIView):
    city_service = CityService()

    # GET /v1/cities/
    def get(self, request) -> JsonResponse:
        city_list = self.city_service.fetch_city_list()

        return JsonResponse(city_list, safe=False)
