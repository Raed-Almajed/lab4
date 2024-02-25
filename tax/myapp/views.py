from operator import index
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rate = 0.15
percent_rate = 15

def index(request):
    return HttpResponse("<h1>this is a site to calculate tax")

def calc(request, num):
    return HttpResponse(f"<h1>your total is {num * rate+ num }")

def tax_rate(request):
    return render(request, "myapp/tax_rate.html", {"rate": percent_rate} )