from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def administrator_page(request):
    text = "<h1>Bu admin sahifasi</h1><h2>Bu bosh sahifa</h2>"
    return HttpResponse(text)
