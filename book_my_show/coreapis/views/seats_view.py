from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.seats_service import SeatService
from dependency_injector.wiring import inject, Provide
from book_my_show.containers.service_container import ServiceContainer
from book_my_show.coreapis.services.seats_service import ISeatService


class SeatView(APIView):
    # GET v1/showtimes/<str:id>/seats/
    def get(
        self,
        request,
        id: str,
        seat_service: ISeatService = Provide[ServiceContainer.seats_service],
    ) -> JsonResponse:
        showtime_pk = id
        seat_type = None

        if "seat_type" in request.GET:
            seat_type = request.GET["seat_type"]

        try:
            seats = seat_service.get_seat_by_seat_type(seat_type, showtime_pk)
        except:
            seats = "Invalid Seat Type"

        return JsonResponse(seats, safe=False)
