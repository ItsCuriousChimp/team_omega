from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.city_service import CityService
from dependency_injector.wiring import inject, Provide
from book_my_show.containers import Services


class CityView(APIView):

    # GET /v1/cities/
    @inject
    def get(
        self,
        request,
        city_service: CityService = Provide[Services.city_service],
    ) -> JsonResponse:
        city_list = city_service.fetch_city_list()

        return JsonResponse(city_list, safe=False)
