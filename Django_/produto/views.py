from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def metodo(request):
    return render(request, 'produto/index.html')
