from django.shortcuts import render
from .models import contact
# Create your views here.
# def contact_view(request):
#     return render(request,"contact.html")


def contact_view(request):
    context = {}
    context["dataset"] = contact.objects.all()
    return render(request, "contact.html", context)
