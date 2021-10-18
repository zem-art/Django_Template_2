from django.shortcuts import render

# Create your views here.


def index(request):
    ctx = {
        "Title": "Contact"
    }
    return render(request, "index.html", ctx)
