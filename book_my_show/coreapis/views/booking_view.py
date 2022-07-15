from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from book_my_show.coreapis.services.booking_service import BookingService
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class BookingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    booking_service = BookingService()

    # POST /v1/showtimes/<str:show_id>/seats/<str:seat_id>/
    def post(self, request, show_id: str, seat_id: str) -> JsonResponse:

        authtoken = request.headers.get("Authorization")[6:]
        user_id = Token.objects.get(key=authtoken).user
        user_details = self.booking_service.get_user_name((user_id.pk))
        seat_available = self.booking_service.is_seat_available(show_id, seat_id)
        response_dict = {}

        if seat_available:
            self.booking_service.create_booking(user_id, show_id, seat_id)
            booking_status = "Congratulations! Seat Booked."
            response_dict["Booking Details"] = {
                "Show_id": str(show_id),
                "Seat_Id": str(seat_id),
            }
        else:
            booking_status = "Seat not available"

        response_dict["Status"] = booking_status
        response_dict["User_Details"] = user_details

        return JsonResponse(response_dict)
