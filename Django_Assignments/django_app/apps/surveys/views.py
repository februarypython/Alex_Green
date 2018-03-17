from django.shortcuts import render, HttpResponse, redirect

def surveys(request):
    response = "These are all of the created surveys"
    return HttpResponse(response)

def surveys_new(request):
    response = "This is where users will create new surveys"
    return HttpResponse(response)