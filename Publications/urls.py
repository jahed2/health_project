from django.urls import path

from Publications import views 

urlpatterns = [
    path("",views.public, name="public"),
]