
from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

# Create your views here.

def index(request):
    try:
        request.session['total_gold']
    except KeyError:
        request.session['total_gold'] = 0
    return render(request, 'ninjagold/index.html')

def process(request):
    try:
        temp = request.session['activity']
    except:
        temp = []

    if request.POST['building'] == 'farm':
        result = random.randrange(10, 21)

    if request.POST['building'] == 'cave':
        result = random.randrange(5, 11)
    
    if request.POST['building'] == 'house':
        result = random.randrange(2, 6)

    if request.POST['building'] == 'casino':
        result = random.randrange(-50, 50)
    
    if result > 0:
        message = "You earned {} gold at the {} @ {}".format(result, request.POST['building'], datetime.now().strftime("%H:%m:%S %p"))
    
    else:
        message = "You lost {} gold at the {} @ {}".format(result, request.POST['building'], datetime.now().strftime("%H:%m:%S %p"))
    
    temp.append(message) 
    request.session['activity'] = temp
    request.session['total_gold'] += result
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect("/")