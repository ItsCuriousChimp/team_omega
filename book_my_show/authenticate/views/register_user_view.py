from rest_framework.views import APIView
from rest_framework.response import Response
from book_my_show.authenticate.services.register_user_service import RegisterUserService


class RegisterUserView(APIView):
    def post(self, request) -> Response:

        register_user_service = RegisterUserService()
        resp = register_user_service.create_user(request.data)

        return Response(resp)
