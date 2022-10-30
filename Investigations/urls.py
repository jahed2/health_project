from django.urls import path

from .views import investigations

urlpatterns = [
    path("",investigations, name="investigations"),
]