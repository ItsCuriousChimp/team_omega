# from django.shortcuts import render
from django.http import JsonResponse
from ..services.heartbeat_service import HeartbeatService


class HeartbeatView:
    def get_heartbeat(self):
        heartbeat_service = HeartbeatService()
        return JsonResponse({"Heartbeat": heartbeat_service.get_heartbeat()})
