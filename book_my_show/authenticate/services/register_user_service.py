import json
from shutil import register_unpack_format

from yaml import serialize
from book_my_show.authenticate.repositories.register_user_repositry import (
    RegisterUserRepository,
)


class RegisterUserService:
    def create_user(self, data) -> json:
        resp = {}
        register_user_repo = RegisterUserRepository()
        serializer = register_user_repo.get_serializer(data)
        try:
            if serializer.is_valid():
                register_user_repo.create_user_db(serializer)
                resp["email"] = serializer.validated_data["email"]
                resp["message"] = "User Registered Successfully"
            else:
                resp = serializer.errors
        except Exception as error:
            resp = {"message": str(error)}

        return resp
