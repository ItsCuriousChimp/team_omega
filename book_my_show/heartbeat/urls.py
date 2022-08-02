from django.urls import path
from book_my_show.heartbeat.views.heartbeat_view import HeartbeatView

urlpatterns = [path("", HeartbeatView.as_view())]
