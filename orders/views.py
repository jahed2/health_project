from django.shortcuts import render
from .models import order
# Create your views here.


def order_view(request):
    context = {}
    context["dataset"] = order.objects.all()
    return render(request, 'orders.html', context)
