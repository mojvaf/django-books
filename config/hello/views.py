from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, welcome to the Hello app!")

def greetings(request):
    context = {'name':'Moj', 'lastName':'last' ,'message': 'Welcome'}
    return render(request, 'hello/greetings.html', context)