from django.shortcuts import render

# Create your views here.


def link_view(request):
    return render(request, 'links.html')
