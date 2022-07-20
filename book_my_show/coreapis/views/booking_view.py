from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from dependency_injector.wiring import inject, Provide
from book_my_show.containers.service_container import ServiceContainer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from book_my_show.coreapis.services.booking_service import IBookingService


class BookingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # POST /v1/showtimes/<str:show_id>/seats/<str:seat_id>/
    def __init__(
        self,
        booking_service: IBookingService = Provide[ServiceContainer.booking_service],
    ) -> None:
        self.booking_service = booking_service

    @inject
    def post(
        self,
        request,
        show_id: str,
        seat_id: str,
    ) -> JsonResponse:
        authtoken = request.headers.get("Authorization")[6:]
        user_id = Token.objects.get(key=authtoken).user
        seat_available = self.booking_service.is_seat_available(show_id, seat_id)
        response_dict = {}

        if seat_available:
            self.booking_service.create_booking(user_id, show_id, seat_id)

        response_dict = self.booking_service.get_booking_response(
            seat_available, user_id, show_id, seat_id
        )

        return JsonResponse(response_dict)
