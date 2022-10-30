from django.contrib import admin
from django.urls import path
from .views import circular_view

urlpatterns = [
    path("", circular_view, name="circular_view"),
]
