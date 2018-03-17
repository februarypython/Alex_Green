from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'surveyform/index.html')

def create(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['favlang'] = request.POST['favlang']
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comment']
        return redirect("/process")

def welcome(request):
    request.session['counter'] += 1
    return render(request, 'surveyform/welcome.html')
# Create your views here.
