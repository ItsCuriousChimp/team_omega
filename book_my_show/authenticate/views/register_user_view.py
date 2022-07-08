# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

# from django.contrib.auth.models import User
from book_my_show.authenticate.models.user_model import UserModel
from book_my_show.authenticate.serializers.registration_serializer import (
    RegistraionSerializer,
)
from rest_framework.response import Response
from book_my_show.authenticate.services.register_user_service import RegisterUserService


class RegisterUserView(APIView):
    def post(self, request):

        register_user_service = RegisterUserService()
        resp = register_user_service.create_user(request.data)

        return Response(resp)
