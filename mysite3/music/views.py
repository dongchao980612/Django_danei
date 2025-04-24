from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def index_view(request):
    return render(request, "music/index.html")
