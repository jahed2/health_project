from django.contrib import admin
from django.urls import path
from .views import departments

urlpatterns = [
    path('', departments, name='department')
]
