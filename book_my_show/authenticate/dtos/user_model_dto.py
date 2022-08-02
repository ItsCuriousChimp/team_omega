from datetime import datetime


class UserModelDto:
    email: str
    last_login: datetime
    first_name: str
    last_name: str
    address: str
    phone_no: str
    password: str

    def __init__(
        self,
        email,
        password,
        first_name=None,
        last_name=None,
        address=None,
        phone_no=None,
    ) -> None:

        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_no = phone_no
