from django.contrib import admin
from django.urls import path, include
from .api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ninja/", api.urls),
    path("drf/", include("projects.drf.urls")),
]
