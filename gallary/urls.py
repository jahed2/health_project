from django.urls import path

from .views import Imageview

urlpatterns = [
    path("", Imageview.as_view(), name="image"),
]
