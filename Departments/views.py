from django.shortcuts import render
from .models import department
# Create your views here.


# def dept_view(request):
#     return render(request, "dept.html")

def departments(request):
    context = {}
    context["dataset"] = department.objects.all()
    return render(request, "department.html", context)
