from rest_framework.views import APIView
from rest_framework.response import Response
from book_my_show.authenticate.services.authentication_service import (
    AuthenticationService,
)


class LoginUserView(APIView):
    def post(self, request) -> Response:

        login_service = AuthenticationService()
        response = login_service.verify_credentials(request.data)

        return Response(response)
