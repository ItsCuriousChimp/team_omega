# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

# from django.contrib.auth.models import User
from book_my_show.authenticate.models.user_model import UserModel


class RegisterUser(APIView):
    def post(self, request):

        email = request.data["email"]
        password = request.data["password"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        address = request.data["address"]
        phone_no = request.data["phone_no"]

        try:
            user = UserModel.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone_no=phone_no,
            )

        except:
            return JsonResponse({"message": "error occured"})

        user.save()

        return JsonResponse(
            {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "address": address,
                "phone_no": phone_no,
                "message": "user successfully created",
            }
        )

        # basic auth
        # try:
        #     user = User.objects.create_user(
        #         email=email,
        #         password=password,
        #         first_name=first_name,
        #         last_name=last_name,
        #         address=address,
        #     )
        # except:
        #     return JsonResponse({"message": "already exists"})
        # user.save()
        # return JsonResponse(
        #     {
        #         "email": email,
        #         "first_name": first_name,
        #         "last_name": last_name,
        #         "message": "user successfully created",
        #     }
        # )
