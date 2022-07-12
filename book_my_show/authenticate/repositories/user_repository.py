from book_my_show.authenticate.serializers.user_serializer import (
    UserSerializer,
)


class UserRepository:
    def get_serializer(self, data) -> UserSerializer:
        serializer = UserSerializer(data=data)

        return serializer

    def create_user_db(self, serializer):
        try:
            serializer.save()
        except:
            raise Exception("Unable to save.Server Error!!")
