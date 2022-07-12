from django.urls import path
from book_my_show.authenticate.views import register_user_view
from rest_framework.authtoken import views


urlpatterns = [
    path("register/", register_user_view.RegisterUserView.as_view()),
    path("login/", views.obtain_auth_token),
]
