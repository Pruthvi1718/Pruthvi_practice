from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    template = 'index.html'






    return render(request, template)



def about(request):
    return HttpResponse("<h1>Welcome to My About Page</h1>")
