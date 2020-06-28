from django.shortcuts import render
from django.http import request, HttpResponse
from iqbot.dankiq import *


# Create your views here.
def landing(request):
    if request.method == "GET":
        return render(request, "index.html")

def home(request):
    if request.method == "GET":
        return render(request, "index.html")