from book_my_show.authenticate.serializers.registration_serializer import RegistraionSerializer


class RegisterUserRepository:
    def get_serializer(self,data):
        print(data)
        serializer=RegistraionSerializer(data=data)


        return serializer
    def create_user_db(self,serializer):
        try:
            serializer.save()
        except Exception as error_message:
            raise Exception("Unable to save.Server Error!!")
    