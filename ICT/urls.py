from django.contrib import admin
from django.urls import path
from .views import ict_view

urlpatterns = [
    path('', ict_view, name='ict')
]
