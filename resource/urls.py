from django.contrib import admin
from django.urls import path
from .views import resource_view

urlpatterns = [
    path("", resource_view, name="resource_view"),
]
