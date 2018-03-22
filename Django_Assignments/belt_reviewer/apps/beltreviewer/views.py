# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    request.session.clear()
    return render(request, 'beltreviewer/index.html')

def validate(request):
    validations = User.objects.validate(request.POST)
    if len(validations) == 0:
        pw = request.POST['password']
        User.objects.create(
            name = request.POST['name'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        )
        request.session['user'] = request.POST['email']
        print "successful registration"
        return redirect("/books/success")
    else:
        for error in validations:
            messages.add_message(request, messages.INFO, error)
            print error
            return redirect("/")

def login(request):
    try:
        user = User.objects.get(email = request.POST['email'])
        pw = request.POST['password'] 
        pw2 = user.password
        request.session['user'] = user.email 
        if bcrypt.checkpw(pw.encode(), pw2.encode()) == True:
            return redirect("/books/success")
        else:
            messages.add_message(request, messages.INFO, "Invalid Login")
            return redirect("/")
    except:
        messages.add_message(request, messages.INFO, "Invalid Login")
        return redirect("/")


    

    

