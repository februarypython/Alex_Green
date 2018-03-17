from django.shortcuts import render, HttpResponse, redirect

def register(request):
    response = "This is where new user records will be displayed"
    return HttpResponse(response)

def login(request):
    response = "This is where users will login"
    return HttpResponse(response)

def users(request):
    response = "Display all users"
    return HttpResponse(response)