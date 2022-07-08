import imp
from book_my_show.authenticate.models.user_model import UserModel
from book_my_show.authenticate.dtos.user_model_dto import UserModelDto
class UserModelRepository:
    def get_user_credentials(self,email):
        model_details = UserModel.objects.get(email=email)
        user_model_dto=UserModelDto(email=model_details.email,password=model_details.password)
        print(user_model_dto)
        return user_model_dto

