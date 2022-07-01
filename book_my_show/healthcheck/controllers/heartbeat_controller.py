# from django.shortcuts import render
from django.http import JsonResponse
from ..services.heartbeat_service import HeartBeatService


class HeartBeat:
    def get_heartbeat(self):
        heart_beat = HeartBeatService()
        return JsonResponse({"Heartbeat": heart_beat.get_heartbeat_dto()})
