# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def index(request):
    return render(request, 'log_reg/index.html')

def sign_in(request):
    return render(request, 'log_reg/sign_in.html')

def register(request):
    return render(request, 'log_reg/registration_page.html')

def process_registration(request):
    validation = User.objects.validate(request.POST)
    print validation
    
    if len(validation[0]) > 0:
        for error in validation[0]:
            messages.add_message(request, messages.INFO, error)           
        return redirect("/register")
    else:
        request.session['user_id'] = validation[1].id
        print request.session['user_id']
        return redirect("/register")

