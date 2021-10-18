from django.shortcuts import render

# Create your views here.


def index(request):
    ctx = {
        "Title": "Dashboard",
    }
    return render(request, 'home/index.html', ctx)
