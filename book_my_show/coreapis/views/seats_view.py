from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.seats_service import SeatService
from dependency_injector.wiring import Provide
from book_my_show.containers.service_container import ServiceContainer
from book_my_show.coreapis.services.seats_service import ISeatService


class SeatView(APIView):
    def __init__(
        self,
        seat_service: ISeatService = Provide[ServiceContainer.seats_service],
    ) -> None:
        self.seat_service = seat_service

    # GET v1/showtimes/<str:id>/seats/
    def get(
        self,
        request,
        id: str,
    ) -> JsonResponse:
        showtime_id = id
        seat_availability = None

        if "seat_availability" in request.GET:
            seat_availability = request.GET["seat_availability"]

        try:
            seats = self.seat_service.get_seat_by_seat_type(
                seat_availability, showtime_id
            )
        except:
            seats = "Invalid Seat Type"

        return JsonResponse(seats, safe=False)
