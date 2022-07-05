# from django.urls import URLPattern
from django.urls import path
from .views import heartbeat_view

urlpatterns = [path("", heartbeat_view.HeartbeatView.get_heartbeat)]
