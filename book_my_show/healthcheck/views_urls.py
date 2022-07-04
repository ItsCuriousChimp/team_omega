# from django.urls import URLPattern
from django.urls import path
from .views import heartbeat_views

urlpatterns = [path("", heartbeat_views.Heartbeat.get_heartbeat)]
