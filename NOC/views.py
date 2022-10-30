from django.shortcuts import render
from .models import Noc
# Create your views here.
def noc_view(request):
    context = {}
    context["dataset"] = Noc.objects.all()
    return render(request,'noc.html',context)