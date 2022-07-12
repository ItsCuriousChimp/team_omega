import json
from django.contrib.auth import authenticate


class AuthenticationService:
    def verify_credentials(self, user_data) -> json:
        resp: str = "Login Successful"

        try:
            user = authenticate(
                username=user_data["email"], password=user_data["password"]
            )

            if user is None:
                raise Exception("wrong credentials ")

        except Exception as error_msg:
            resp = error_msg

        return {"message": str(resp)}
