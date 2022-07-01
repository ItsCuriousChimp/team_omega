# from django.urls import URLPattern
from django.urls import path
from .controllers import heartbeat_controller

urlpatterns = [path("", heartbeat_controller.HeartBeat.get_heartbeat)]
