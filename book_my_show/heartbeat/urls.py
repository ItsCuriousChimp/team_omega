# from django.urls import URLPattern
from django.urls import path
from book_my_show.heartbeat.views.heartbeat_view import HeartbeatView

urlpatterns = [path("", HeartbeatView.get_heartbeat)]
