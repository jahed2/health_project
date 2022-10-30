from django.shortcuts import render
from .models import Resource
# Create your views here.


def resource_view(request):
    context = {}
    context["dataset"] = Resource.objects.all()
    return render(request, 'resource.html', context)
