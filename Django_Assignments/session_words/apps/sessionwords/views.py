from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'sessionwords/index.html')

def submit(request):
    try:
        temp = request.session['words'] #set temp to session words if it exists. if not,
    except KeyError:
        temp = [] #set temp variable to empty list
    if 'big_font' in request.POST: #if big font checkbox is checked, set the font variable accordingly
		font = "big"
    else:
        font = "normal"
    word = {"word": request.POST['words'], 
            "color": request.POST['color'],
            "time": datetime.strftime(datetime.now(), "%H:%M:%S %p, %B %d, %Y"),
            "font": font}
    temp.append(word) #append the word dictionary to temp variable, either empty list or existing sesion words list
    request.session['words'] = temp #set session words back to temp variable
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
