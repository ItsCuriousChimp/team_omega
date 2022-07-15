from tokenize import Token
from django.http import JsonResponse
from book_my_show.heartbeat.services.heartbeat_service import HeartbeatService
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class HeartbeatView(APIView):
    # GET /v1/heartbeat/
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request) -> JsonResponse:
        heartbeat_service = HeartbeatService()
        heartbeat = heartbeat_service.get_heartbeat()
        return JsonResponse(
            {"timestamp": heartbeat.last_beat_at.strftime("%m/%d/%Y, %H:%M:%S")}
        )
