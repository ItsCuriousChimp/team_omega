from rest_framework import serializers
from book_my_show.authenticate.models.user_model import UserModel
class RegistraionSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields='__all__'
    def	save(self):
        user_model = UserModel(
					email=self.validated_data['email'],
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                    address=self.validated_data['address'],
                    phone_no=self.validated_data['phone_no'],
				)
        password = self.validated_data['password']
        user_model.set_password(password)
        user_model.save()
        return user_model
