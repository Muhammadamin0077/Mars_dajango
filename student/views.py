from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student_page(request):
    text = "<h1>Bu studdent sahifasi</h1>"
    return HttpResponse(text)
