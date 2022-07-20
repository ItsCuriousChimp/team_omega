from django.http import JsonResponse
from rest_framework.views import APIView
from dependency_injector.wiring import inject, Provide
from book_my_show.containers.service_container import ServiceContainer
from book_my_show.coreapis.services.city_service import ICityService


class CityView(APIView):
    # GET /v1/cities/
    def __init__(
        self,
        city_service: ICityService = Provide[ServiceContainer.city_service],
    ) -> None:
        self.city_service = city_service

    @inject
    def get(
        self,
        request,
    ) -> JsonResponse:
        city_list = self.city_service.fetch_city_list()

        return JsonResponse(city_list, safe=False)
