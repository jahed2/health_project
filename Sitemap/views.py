from django.shortcuts import render

# Create your views here.


def site_view(request):
    return render(request, 'site.html')
