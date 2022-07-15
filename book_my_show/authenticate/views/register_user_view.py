import json
from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.authenticate.services.user_service import UserService
from book_my_show.authenticate.serializers.user_serializer import UserSerializer


class RegisterUserView(APIView):

    # POST /v1/register
    def post(self, request) -> JsonResponse:

        register_user_service = UserService()
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            resp: json = register_user_service.create_user(serializer)
        else:
            resp: json = serializer.errors

        return JsonResponse(resp)
