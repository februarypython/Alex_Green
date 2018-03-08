from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "List of Blogs"
    return HttpResponse(response)

def new(request):
    response = "This will be a form page to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse("Blog #" + number)

def edit(request, number):
    return HttpResponse("Edit Blog #" + number)

def destroy(request, number):
    return redirect("/")