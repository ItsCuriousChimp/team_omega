import imp
from django.urls import URLPattern, path
from .views import heartbeat_view

urlpatterns = [
    path('', heartbeat_view.HeartBeat.get_heartbeat)
]
