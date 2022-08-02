import json
from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.authenticate.services.user_service import IUserService
from book_my_show.authenticate.serializers.user_serializer import UserSerializer
from book_my_show.containers.service_container import ServiceContainer
from dependency_injector.wiring import Provide


class RegisterUserView(APIView):
    def __init__(
        self,
        register_user_service: IUserService = Provide[
            ServiceContainer.register_service
        ],
    ) -> None:
        self.register_user_service: IUserService = register_user_service

    # POST /v1/register
    def post(self, request) -> JsonResponse:

        serializer: UserSerializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            resp: json = self.register_user_service.create_user(serializer)
        else:
            resp: json = serializer.errors

        return JsonResponse(resp)
