import json
from book_my_show.authenticate.repositories.user_repository import UserRepository

from rest_framework.authtoken.models import Token

from book_my_show.authenticate.serializers.user_serializer import UserSerializer


class UserService:
    def create_user(self, serializer: UserSerializer) -> json:
        resp: json = {}
        register_user_repo = UserRepository()
        phone_no: str = serializer.validated_data["phone_no"]
        first_name: str = serializer.validated_data["first_name"]
        last_name: str = serializer.validated_data["last_name"]
        full_name: str = ""
        if first_name or last_name:
            full_name: str = first_name + last_name

        register_user_repo.create_user_db(serializer)

        resp["email"] = serializer.validated_data["email"]
        resp["Mobile Number"] = phone_no if phone_no != None else ""
        resp["Full Name"] = full_name
        token = Token.objects.get(user=resp["email"]).key
        data["token"] = token

        return resp
