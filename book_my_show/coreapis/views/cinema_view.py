from django.http import JsonResponse
from rest_framework.views import APIView
from book_my_show.containers.service_container import ServiceContainer
from dependency_injector.wiring import Provide
from book_my_show.coreapis.dtos.cinema_dto import CinemaDto
from book_my_show.coreapis.services.cinema_service import ICinemaService


class CinemaView(APIView):
    def __init__(
        self,
        cinema_service: ICinemaService = Provide[ServiceContainer.cinema_service],
    ) -> None:
        self.cinema_service = cinema_service

    # GET /v1/movies/<str:id>/cinemas/
    def get(
        self,
        request,
        id: str,
    ) -> JsonResponse:
        movie_id = id
        allcinemas_playing_movies: dict[
            list[CinemaDto]
        ] = self.cinema_service.get_cinemas(movie_id)

        dict_response = self.DictResponse(allcinemas_playing_movies)

        return JsonResponse(dict_response)

    def DictResponse(self, all_cinema_dto: CinemaDto) -> dict:
        all_cinema_dict = {}

        for cinema_id in all_cinema_dto:
            all_cinema_dict[cinema_id] = []
            for cinema in all_cinema_dto.get(cinema_id):
                cinema_dict = {}
                cinema_dict["showtime_id"] = cinema.showtime_id
                cinema_dict["start_time_at_utc"] = cinema.start_time_at_utc.strftime(
                    "%m/%d/%Y, %H:%M:%S"
                )
                cinema_dict["end_time_at_utc"] = cinema.end_time_at_utc.strftime(
                    "%m/%d/%Y, %H:%M:%S"
                )
                all_cinema_dict[cinema_id].append(cinema_dict)

        return all_cinema_dict
