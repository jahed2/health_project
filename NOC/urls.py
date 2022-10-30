from django.contrib import admin
from django.urls import path
from .views import noc_view

urlpatterns = [
        path("",noc_view, name="noc_view"),
]
