from django.urls import path
from book_my_show.coreapis.views.cinema_view import CinemaView
from book_my_show.coreapis.views.alltable_views import AllTable


urlpatterns = [
    path("alltables/", AllTable.as_view()),
    path("movies/<str:pk1>/", CinemaView.as_view()),
]
