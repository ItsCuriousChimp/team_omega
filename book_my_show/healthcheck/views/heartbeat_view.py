from django.shortcuts import render
from django.http import JsonResponse
from ..services.heartbeat_service import HeartBeatService 

class HeartBeat:
    
    def get_heartbeat(request, *args, **kwargs): 
        heart_beat = HeartBeatService.get_heartbeat_dto()
        return JsonResponse({"Heartbeat":heart_beat})
