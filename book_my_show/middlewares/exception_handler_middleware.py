from django.http import HttpResponse, JsonResponse
from book_my_show.common.enums.app_environment import AppEnvironment
from django.conf import settings
import logging

logging.basicConfig(
    filename="/team_omega/book_my_show/common/log/debug.log",
    filemode="a",
    level=logging.ERROR,
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class ExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logging.error(exception)
        if settings.APP_ENVIRONMENT != AppEnvironment.Local:
            return JsonResponse({"Result": "Failed", "Output": "Error occured"})
        return HttpResponse(exception)
