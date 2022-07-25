from abc import ABC, abstractmethod
from book_my_show.authenticate.serializers.user_serializer import (
    UserSerializer,
)

class IUserRepository(ABC):
    @abstractmethod
    def create_user_db(self):
        raise NotImplementedError('Abstract method not implemented.')


class UserRepository(IUserRepository):
    def create_user_db(self, serializer: UserSerializer) -> None:
        serializer.save()
