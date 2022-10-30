from django.shortcuts import render
from .models import Notice
# Create your views here.


def notice_view(request):
    context = {}
    context["dataset"] = Notice.objects.all()
    return render(request, 'notice.html', context)
