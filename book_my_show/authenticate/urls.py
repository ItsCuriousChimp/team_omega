# from django.urls import URLPattern
from django.urls import path
from book_my_show.authenticate.views import login_user_view, register_user_view

urlpatterns = [
    path("register/", register_user_view.RegisterUser.as_view()),
    path("login/", login_user_view.LoginUserView.as_view()),
]
