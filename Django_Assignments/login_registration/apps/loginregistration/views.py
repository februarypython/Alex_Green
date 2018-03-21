# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User
import bcrypt

# Create your views here.
def index(request):
    request.session.clear()
    return render(request, 'loginregistration/index.html')

def validate_reg(request):
    validations = User.objects.validate(request.POST)
    if len(validations) == 0:
        password = request.POST['password']
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        )
        print "success"
        request.session['user'] = request.POST['email']
        return redirect("/success")
    else:
        for error in validations:
            messages.add_message(request, messages.INFO, error)
            print error
            return redirect ("/")

def login(request):
    user = User.objects.get(email = request.POST['email'])
    pw = request.POST['password'] # i found bcrypt to only work when passwords set to variables
    pw2 = user.password
    request.session['user'] = user.email #set a session to the email of the user logging in
    if bcrypt.checkpw(pw.encode(), pw2.encode()) == True:
        print user.first_name, user.last_name
        return redirect("/success")
    else:
        messages.add_message(request, messages.INFO, "Invalid login credentials")
    return redirect("/")

def success(request):
    context = {"user": User.objects.get(email=request.session['user'])} #context dictionary works for new registrations and logins
    return render(request, 'loginregistration/success.html', context)
 
