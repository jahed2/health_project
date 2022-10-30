from django.contrib import admin
from django.urls import path
from .views import link_view

urlpatterns = [
    path('', link_view, name='link')
]
