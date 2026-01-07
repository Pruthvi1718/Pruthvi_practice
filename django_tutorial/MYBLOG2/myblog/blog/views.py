from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to My Blog</h1>")


# def home(request):
#     return HttpResponse("<h1>Welcome to My Contact Page</h1>")

# def home(request):
#     return HttpResponse("<h1>Welcome to My Blog Page</h1>")