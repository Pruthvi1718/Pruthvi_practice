from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


def home(request):
    template = 'index.html'

    data = {
           "Karnataka": "Bengaluru",
           "Maharashtra": "Mumbai",
           "Goa": "Panaji",
           "UP": "Lucknow",
    }

    return render(request, template, {"context":data})



def about(request):
    template = 'about.html'
    return render(request, template)

# def contact(request):
#     template = 'contact.html'
#     return render(request, template)

select * from blogs
def blogs list(request):

