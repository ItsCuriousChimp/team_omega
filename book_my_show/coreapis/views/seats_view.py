from rest_framework.views import APIView
from rest_framework.views import Response
from book_my_show.coreapis.services.seats_service import SeatService


class SeatView(APIView):
    seat_service = SeatService()

    def get(self, request, id: str) -> Response:
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
            seats = "invalid seat type"

        return Response(seats)
