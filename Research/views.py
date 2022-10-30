from django.shortcuts import render
from .models import ResumeModel
# Create your views here.
# def resume(request):
#     resume = ResumeModel.objects.last() # < Not sure if this part is needed?
#     return render(request, 'research.html', context={'resume':resume})

def resume(request):
    context = {}
    context["dataset"] = ResumeModel.objects.all()
    return render(request,"research.html",context)