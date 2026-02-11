<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======

from django.shortcuts import render
from django.http import HttpResponse
def hello_view(request):
    return render(request, 'index.html')
>>>>>>> 37f8d0ce094c960921418dff1a5568ea3433b6d1
