from django.contrib import admin
from django.urls import path
from .views import site_view

urlpatterns = [
    path('', site_view, name='site')
]
