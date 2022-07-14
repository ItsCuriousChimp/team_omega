from django.urls import path
from book_my_show.coreapis.views.cinema_view import CinemaView
from book_my_show.coreapis.views.alltable_views import AllTable
from book_my_show.coreapis.views.movie_in_city import MovieInCity


urlpatterns = [
    path("alltables/", AllTable.as_view()),
    path("movies/<str:pk1>/", CinemaView.as_view()),
    path("movies/city/<str:pk>", MovieInCity.as_view()),
]
