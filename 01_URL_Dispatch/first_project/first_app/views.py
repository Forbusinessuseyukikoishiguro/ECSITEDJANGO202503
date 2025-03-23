from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Good Bye</h1>')

def user_page(request, user_name):
    print(type(user_name),user_name)
    return HttpResponse(f'<h1>{user_name}Page</h1>')