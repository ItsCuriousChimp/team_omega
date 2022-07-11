from django.http import HttpResponse, JsonResponse
from book_my_show.common.enums.app_environment import AppEnvironment
from django.conf import settings


class ExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):

        if settings.APP_ENVIRONMENT != AppEnvironment.Local:
            return JsonResponse({"Result": "Failed", "Output": "Error occured"})
        return HttpResponse(exception)
