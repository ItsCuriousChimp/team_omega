from turtle import pen
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.authtoken.models import Token


class BookingView(APIView):
    # GET /v1/movies/<str:id>/cinema/

    def post(self, request, pk1, pk2) -> JsonResponse:
        authtoken = request.headers.get("Authorization")[6:]
        # print(auth)
        # show_id = pk1
        # seat_id = pk2
        user = Token.objects.get(key=authtoken).user
        print(user)

        return Response("hi")
