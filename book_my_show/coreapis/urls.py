from django.urls import path

from book_my_show.coreapis.views.seats_view import SeatView


urlpatterns = [
    path("showtimes/<str:id>/", SeatView.as_view()),
]
