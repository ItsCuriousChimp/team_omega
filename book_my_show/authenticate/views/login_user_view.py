# from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginUser(APIView):
    def post(self, request):

        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            return JsonResponse({"username": username, "message": "login successful"})

        return JsonResponse({"message": "wrong details"})
