from rest_framework.views import APIView
from rest_framework.views import Response
from book_my_show.coreapis.services.seat_available_service import SeatRepository


class SeatAvailableView(APIView):
    def get(self, request, id):
        showtime_pk = id
        seat_available_service = SeatRepository()
        seat_available_of_showtime = seat_available_service.get_seat_available(
            showtime_pk
        )
        return Response(seat_available_of_showtime)
