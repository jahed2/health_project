from django.contrib import admin
from django.urls import path
from .views import order_view

urlpatterns = [
    path("", order_view, name="order_view"),
]
