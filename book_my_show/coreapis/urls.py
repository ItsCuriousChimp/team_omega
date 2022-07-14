from django.urls import path
from book_my_show.coreapis.views.booking_view import BookingView
from book_my_show.coreapis.views.cinema_view import CinemaView


urlpatterns = [
    path("movies/<str:id>/cinemas/", CinemaView.as_view()),
    path("showtime/<str:pk1>/seat/<str:pk2>/", BookingView.as_view()),
]
