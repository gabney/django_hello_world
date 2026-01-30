from django.shortcuts import render

# Create your views here.
from .models import Greeting

def hello_world(request):
    greeting = Greeting.objects.first()
    return render(request, "hello.html", {"greeting": greeting})
