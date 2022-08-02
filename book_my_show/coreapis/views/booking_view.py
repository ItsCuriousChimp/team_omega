from django.http import JsonResponse
from rest_framework.views import APIView
from dependency_injector.wiring import Provide
from book_my_show.containers.service_container import ServiceContainer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from book_my_show.coreapis.services.booking_service import IBookingService
from book_my_show.coreapis.dtos.booking_model_dto import BookingModelDto


class BookingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(
        self,
        booking_service: IBookingService = Provide[ServiceContainer.booking_service],
    ) -> None:
        self.booking_service: IBookingService = booking_service

    # POST /v1/showtimes/<str:show_id>/seats/<str:seat_id>/
    def post(
        self,
        request,
        show_id: str,
        seat_id: str,
    ) -> JsonResponse:
        authtoken: str = request.headers.get("Authorization")[6:]

        booking_status_dto: BookingModelDto = self.booking_service.verify_booking(
            show_id, seat_id, authtoken
        )
        response_dict: dict = {}
        if booking_status_dto.booking_details_dto:
            response_dict["Booking Details"] = {
                "Show_id": booking_status_dto.booking_details_dto.show_id,
                "Seat_Id": booking_status_dto.booking_details_dto.seat_id,
            }
        response_dict["Status"] = booking_status_dto.booking_status
        response_dict["User_Details"] = booking_status_dto.user_details
        return JsonResponse(response_dict)
