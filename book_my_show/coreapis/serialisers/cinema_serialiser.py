from rest_framework import serializers

from book_my_show.coreapis.models.cinema_model import Cinema
from book_my_show.coreapis.models.showtime_model import Showtime


class ShowtimeSerialiser(serializers.ModelSerializer):
    cinema_name = serializers.SerializerMethodField("get_cinema_name")

    class Meta:
        model = Showtime
        abstract = False
        fields = ["start_time_at_utc", "end_time_at_utc", "id", "cinema_name"]

    def get_cinema_name(self, showtime):
        return showtime.cinema_screen
