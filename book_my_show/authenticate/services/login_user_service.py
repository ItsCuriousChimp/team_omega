from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from book_my_show.authenticate.models.user_model import UserModel


class LoginUserService:
    def verify(self, request):
        resp = "Login Successful"

        try:
            model_details = UserModel.objects.get(email=request.data["email"])

            verify_password = check_password(
                request.data["password"], model_details.password
            )

            if not verify_password:
                raise Exception("wrong password ")

        except Exception as error_msg:
            resp = error_msg

        return JsonResponse({"message": str(resp)})
