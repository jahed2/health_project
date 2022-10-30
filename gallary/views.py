from typing import List
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Image


class Imageview(ListView):
    model = Image
    template_name = "gallary.html"
