from django.contrib import admin
from django.urls import path
from .views import notice_view

urlpatterns = [
    path("", notice_view, name="notice_view"),
]
