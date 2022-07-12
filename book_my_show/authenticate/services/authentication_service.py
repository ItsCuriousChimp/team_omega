import json
from django.contrib.auth import authenticate


class AuthenticationService:
    def verify_credentials(self, user_data) -> json:
        resp: str = "Login Successful"

        user = authenticate(
            username=user_data["email"], password=user_data["password"]
        )

        if user is None:
            resp = "Login Failed"

        return {"message": str(resp)}
