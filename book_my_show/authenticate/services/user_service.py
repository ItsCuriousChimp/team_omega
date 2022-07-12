import json
from shutil import register_unpack_format

from yaml import serialize
from book_my_show.authenticate.repositories.user_repository import (
    UserRepository,
)


class UserService:
    def create_user(self, serializer) -> json:
        resp = {}
        register_user_repo = UserRepository()
        
        register_user_repo.create_user_db(serializer)
        resp["email"] = serializer.validated_data["email"]
        resp["Mobile Number"] = serializer.validated_data["phone_no"]

        return resp
