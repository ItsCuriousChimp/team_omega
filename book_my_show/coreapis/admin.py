from django.contrib import admin
from book_my_show.coreapis.models import (
    booking_model,
    cinema_model,
    cinema_screen_model,
    city_model,
    movie_model,
    seat_model,
    showtime_model,
)

admin.site.register(booking_model.Booking)
admin.site.register(cinema_model.Cinema)
admin.site.register(cinema_screen_model.CinemaScreen)
admin.site.register(city_model.City)
admin.site.register(movie_model.Movie)
admin.site.register(seat_model.Seat)
admin.site.register(showtime_model.Showtime)
