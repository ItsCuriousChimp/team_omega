from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

# from book_my_show.coreapis.containers.container import Container
from book_my_show.coreapis.services.booking_service import (
    BookingService,
    ResponseMaker,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from dependency_injector.wiring import inject, Provide


class BookingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    booking_service = BookingService()
    response_maker = ResponseMaker()

    # POST /v1/showtimes/<str:show_id>/seats/<str:seat_id>/
    @inject
    def post(
        self,
        request,
        show_id: str,
        seat_id: str,
    ) -> JsonResponse:

        # check this code
        authtoken = request.headers.get("Authorization")[6:]
        user_id = Token.objects.get(key=authtoken).user

        seat_available = self.booking_service.is_seat_available(show_id, seat_id)
        response_dict = {}

        if seat_available:
            self.booking_service.create_booking(user_id, show_id, seat_id)
            response_dict = self.response_maker.get_booking_response(
                True, user_id, show_id, seat_id
            )
        else:
            response_dict = self.response_maker.get_booking_response(
                False, user_id, show_id, seat_id
            )

        return JsonResponse(response_dict)
