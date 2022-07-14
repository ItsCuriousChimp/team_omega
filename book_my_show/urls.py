from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/heartbeat", include("book_my_show.heartbeat.urls")),
    path("v1/", include("book_my_show.authenticate.urls")),
    path("v1/", include("book_my_show.coreapis.urls")),
]
