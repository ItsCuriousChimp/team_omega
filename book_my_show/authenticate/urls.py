# from django.urls import URLPattern
from django.urls import path
from book_my_show.authenticate.views import register_user, login_user

urlpatterns = [
    path("register/", register_user.RegisterUser.as_view()),
    path("login/", login_user.LoginUser.as_view()),
]
