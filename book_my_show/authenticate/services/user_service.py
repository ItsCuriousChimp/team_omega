from abc import ABC, abstractmethod
import json
from book_my_show.authenticate.repositories.user_repository import IUserRepository
from rest_framework.authtoken.models import Token
from book_my_show.authenticate.serializers.user_serializer import UserSerializer
from book_my_show.containers.repo_container import RepositoryContainer
from dependency_injector.wiring import Provide


class IUserService(ABC):
    @abstractmethod
    def create_user(self):
        raise NotImplementedError("Abstract method not implemented.")


class UserService(IUserService):
    def __init__(
        self,
        register_user_repo: IUserRepository = Provide[
            RepositoryContainer.user_repository
        ],
    ) -> None:
        self.register_user_repo = register_user_repo

    def create_user(self, serializer: UserSerializer) -> json:
        resp: json = {}
        phone_no: str = serializer.validated_data["phone_no"]
        first_name: str = serializer.validated_data["first_name"]
        last_name: str = serializer.validated_data["last_name"]
        full_name: str = ""
        if first_name or last_name:
            full_name: str = first_name + last_name

        self.register_user_repo.create_user_db(serializer)

        resp["email"] = serializer.validated_data["email"]
        resp["Mobile Number"] = phone_no if phone_no is not None else ""
        resp["Full Name"] = full_name
        token = Token.objects.get(user=resp["email"]).key
        resp["token"] = token

        return resp
