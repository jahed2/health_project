from django.shortcuts import render
from .models import circular
# Create your views here.


def circular_view(request):
    context = {}
    context["dataset"] = circular.objects.all()
    return render(request, 'circulars.html', context)
