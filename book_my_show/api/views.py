from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


def heartBeat(request, *args, **kwargs):
    return JsonResponse({"message": "statuscode ok"})
# Create your views here.
