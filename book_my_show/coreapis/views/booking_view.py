from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.authtoken.models import Token
from book_my_show.coreapis.services.booking_service import BookingService
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class BookingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    booking_service = BookingService()

    # POST /v1/showtime/<str:seat_id>/seat/<str:seat_id>/
    def post(self, request, show_id: str, seat_id: str) -> JsonResponse:

        authtoken = request.headers.get("Authorization")[6:]
        user_id = Token.objects.get(key=authtoken).user
        user_details = self.booking_service.get_user_name((user_id.pk))
        seat_available = self.booking_service.is_available(show_id, seat_id)
        resp_dict = {}
        if seat_available:
            self.booking_service.create_booking(user_id, show_id, seat_id)
            resp = "Congratulations! Seat Booked."
            resp_dict["Booking Details"] = {"Show_id":str(show_id), "Seat_Id":str(seat_id)}
        else:
            resp = "Seat not available"
        
        resp_dict["Status"] = resp
        resp_dict["User_Details"] = user_details
        
        return Response(
            resp_dict,
            # safe = False
        )
