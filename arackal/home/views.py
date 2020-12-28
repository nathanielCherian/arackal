from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "home/index.html")

def plumbing(request):
    return render(request, "home/plumbing.html")

def heating(request):
    return render(request, "home/heating.html")

def appliances(request):
    return render(request, "home/appliances.html")