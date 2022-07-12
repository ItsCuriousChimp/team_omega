from book_my_show.authenticate.serializers.user_serializer import (
    UserSerializer,
)


class UserRepository:


    def create_user_db(self, serializer):
        
        serializer.save()
