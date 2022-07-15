from django.urls import path
from book_my_show.coreapis.views.movie_view import MovieList
from book_my_show.coreapis.views.booking_view import BookingView
from book_my_show.coreapis.views.cinema_view import CinemaView
from book_my_show.coreapis.views.seats_view import SeatView


urlpatterns = [
    path("showtimes/<str:id>/seats/", SeatView.as_view()),
    path("cities/<str:id>/movies/", MovieList.as_view()),
    path("movies/<str:id>/cinemas/", CinemaView.as_view()),
    path("showtimes/<str:show_id>/seats/<str:seat_id>/", BookingView.as_view()),
]
