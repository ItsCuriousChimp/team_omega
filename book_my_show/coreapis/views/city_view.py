from django.http import JsonResponse
from rest_framework.views import APIView
from dependency_injector.wiring import Provide
from book_my_show.containers.service_container import ServiceContainer
from book_my_show.coreapis.services.city_service import ICityService
from book_my_show.coreapis.dtos.city_model_dto import CityModelDto


class CityView(APIView):
    def __init__(
        self,
        city_service: ICityService = Provide[ServiceContainer.city_service],
    ) -> None:
        self.city_service = city_service

    # GET /v1/cities/
    def get(
        self,
        request,
    ) -> JsonResponse:
        city_list: list[CityModelDto] = self.city_service.fetch_city_list()
        cities_details: list[dict] = []

        for city in city_list:
            detail = {}
            detail["id"] = city.id
            detail["City_Name"] = city.name
            cities_details.append(detail)

        return JsonResponse(cities_details, safe=False)
