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

        try:
            seats = self.seat_service.get_seat_by_seat_type(seat_type, showtime_pk)
        except:
            seats = "Invalid Seat Type"

        return JsonResponse(seats, safe=False)
