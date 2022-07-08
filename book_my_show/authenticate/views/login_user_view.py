# from django.shortcuts import render
# import imp
# from django.http import HttpResponse, JsonResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from book_my_show.authenticate.services.login_user_service import LoginUserService


class LoginUserView(APIView):
    def post(self, request):

        login_service = LoginUserService()
        response=login_service.verify_credentials(request.data)

        return Response(response)
   