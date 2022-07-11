from book_my_show.authenticate.serializers.registration_serializer import (
    RegistraionSerializer,
)


class RegisterUserRepository:
    def get_serializer(self, data) -> RegistraionSerializer:
        serializer = RegistraionSerializer(data=data)

        return serializer

    def create_user_db(self, serializer):
        try:
            serializer.save()
        except:
            raise Exception("Unable to save.Server Error!!")
