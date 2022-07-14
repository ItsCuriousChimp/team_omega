from django.urls import path

from book_my_show.coreapis.views.seat_available_view import SeatAvailableView


urlpatterns = [
    path("showtimes/<str:id>/seats/", SeatAvailableView.as_view()),
]
