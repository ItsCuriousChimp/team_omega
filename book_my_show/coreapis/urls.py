from django.urls import path
from book_my_show.coreapis.views.movie_view import MovieList
from book_my_show.coreapis.views.cinema_view import CinemaView
from book_my_show.coreapis.views.seats_view import SeatView
from book_my_show.coreapis.views.city_view import CityView

urlpatterns = [
    path("showtimes/<str:id>/seats/", SeatView.as_view()),
    path("city/<str:id>/movies/", MovieList.as_view()),
    path("movies/<str:id>/cinemas/", CinemaView.as_view()),
    path("cities/", CityView.as_view()),
]
