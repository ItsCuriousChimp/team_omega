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

        seat_available = self.booking_service.is_available(show_id, seat_id)

        if seat_available:
            self.booking_service.create_booking(user_id, show_id, seat_id)
            resp = "Congratulations! Seat Booked."
        else:
            resp = "Seat not available"

        return Response(resp)
