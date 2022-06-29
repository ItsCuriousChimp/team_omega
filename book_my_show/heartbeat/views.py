from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def heartBeat_api_response(request):
    return JsonResponse({"status code " : "200 ok"})

    
