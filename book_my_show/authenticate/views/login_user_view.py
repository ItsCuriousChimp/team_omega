# from django.shortcuts import render
# import imp
# from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from book_my_show.authenticate.services.login_user_service import LoginUserService


class LoginUserView(APIView):
    def post(self, request):

        login_service = LoginUserService()
        return login_service.verify(request)

        # basic auth
        # email = request.data["email"]
        # password = request.data["password"]
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     return JsonResponse({"username": username, "message": "login successful"})
        # return JsonResponse({"message": "wrong details"})
