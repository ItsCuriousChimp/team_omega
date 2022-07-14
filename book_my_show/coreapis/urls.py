from django.urls import path
from book_my_show.coreapis.views.cinema_view import CinemaView
from book_my_show.coreapis.views.alltable_views import AllTable
from book_my_show.coreapis.views.movie_view import MovieList

from book_my_show.coreapis.views.seats_view import SeatView


urlpatterns = [
    path("showtimes/<str:id>/", SeatView.as_view()),
    path("alltables/", AllTable.as_view()),
    path("movies/<str:pk1>/", CinemaView.as_view()),
    path("city/<str:id>/movies/", MovieList.as_view()),
]
