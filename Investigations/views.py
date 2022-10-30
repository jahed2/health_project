from django.shortcuts import render
from .models import price
# Create your views here.
def investigations(request):
    context = {}
    context["dataset"] = price.objects.all()
    return render(request,"investigations.html",context)


# def resume(request):
#     context = {}
#     context["dataset"] = ResumeModel.objects.all()
#     return render(request,"research.html",context)