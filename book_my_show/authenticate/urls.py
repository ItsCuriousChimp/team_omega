from django.urls import path
from book_my_show.authenticate.views import login_user_view, register_user_view
from rest_framework.authtoken import views


urlpatterns = [
    path("register/", register_user_view.RegisterUserView.as_view()),
    path("login/", login_user_view.LoginUserView.as_view()),
    path("api-token-auth/", views.obtain_auth_token),
]
