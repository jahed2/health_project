from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import publication

def public(request):
    public = publication.objects.all()
    return render(request,"publications.html",context={'public':public})