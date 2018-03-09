from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    request.session['count'] += 1
    request.session['response'] = get_random_string(length = 20)
    return render(request, 'randomword/index.html')

def generate(request):
    return redirect("/")

def reset(request):
    request.session['count'] = 0
    return redirect("/")

# Create your views here.
