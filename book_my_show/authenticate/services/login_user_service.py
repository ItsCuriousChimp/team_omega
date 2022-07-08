from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from book_my_show.authenticate.models.user_model import UserModel
from rest_framework.authtoken.models import Token
from book_my_show.authenticate.repositories.user_model_repository import UserModelRepository


class LoginUserService:
    def verify_credentials(self, user_data):
        resp = "Login Successful"
        user_model_repo=UserModelRepository()

        try:
            model_details = user_model_repo.get_user_credentials(user_data["email"])
            verify_password = check_password(
                user_data["password"], model_details.password
            )

            if not verify_password:
                raise Exception("wrong password ")

        except Exception as error_msg:
            resp = error_msg

        return {"message": str(resp)}
