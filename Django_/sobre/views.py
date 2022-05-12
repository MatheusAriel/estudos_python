from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'sobre/index.html')


def mais_sobre(request):
    return render(request, 'sobre/mais_sobre.html')