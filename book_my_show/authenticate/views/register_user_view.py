from rest_framework.views import APIView
from rest_framework.response import Response
from book_my_show.authenticate.services.user_service import UserService


class RegisterUserView(APIView):
    def post(self, request) -> Response:

        register_user_service = UserService()
        resp = register_user_service.create_user(request.data)

        return Response(resp)
