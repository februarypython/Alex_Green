# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import regForm, loginForm
from django.shortcuts import render, redirect
from .models import User
import bcrypt

# Create your views here.
def index(request):
    form2 = loginForm() #instances of the log and reg forms from forms.py
    form = regForm()
    context = {
        'form': form,
        'loginForm': form2,
    }
    if request.method == 'POST':
        if request.POST['logreg'] == 'register':
            bound_form = regForm(request.POST) #bound form is a form bound with data
            print bound_form.is_valid()
            print bound_form.errors
            print "="*20, bound_form, "="*20
            if not bound_form.is_valid():
                context['form'] = bound_form
            else:
                bound_form.save()
                request.session['user_id'] = User.objects.get(email=request.POST['email']).id
                print request.session['user_id']
                return redirect("/process")
        if request.POST['logreg'] == 'login':
            bound_form = loginForm(request.POST)
            print bound_form.is_valid()
            print bound_form.errors
            print "++++++++", bound_form, "+++++++++"
            if not bound_form.is_valid():
                context['loginForm'] = bound_form
            else:
                request.session['user_id'] = User.objects.get(email=request.POST['email']).id
                return redirect("/process")

    return render(request, 'login/index.html', context)

def process_registration(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'login/welcome.html', context)
    