from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.coreapis.services.seats_service import SeatService


class SeatView(APIView):
    seat_service = SeatService()

    # GET v1/showtimes/<str:id>/seats/
    def get(self, request, id: str) -> JsonResponse:
        showtime_pk = id
        seat_type = None

        if "seat_type" in request.GET:
            seat_type = request.GET["seat_type"]

        if not seat_type:
            seats = self.seat_service.get_all_seats(showtime_pk)
        elif seat_type == "available":
            seats = self.seat_service.get_seat_available(showtime_pk)
        elif seat_type == "unavailable":
            seats = self.seat_service.get_unavailable_seats(showtime_pk)
        else:
            seats = "Invalid seat type"

        return JsonResponse(seats, safe=False)
