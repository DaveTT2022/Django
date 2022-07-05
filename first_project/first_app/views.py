from django.shortcuts import render, HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse("hello")
def date_and_time(request):
    return HttpResponse(datetime.now())
def intro(request):
    return HttpResponse("welcome to my first django project")
def task(request):
    return HttpResponse(str({x : x * x for x in range(1, 16)}))