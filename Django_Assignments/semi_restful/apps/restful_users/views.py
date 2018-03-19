# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages


# Create your views here.

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, 'restful_users/index.html', context)

def new_user(request):
    return render(request, 'restful_users/new_user.html')

def create(request):
    validations = User.objects.validator(request.POST)
    if len(validations) == 0:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'])
        return redirect("/users")
    else:
        print validations
        for error in validations:
            messages.add_message(request, messages.INFO, error)
            return redirect('/users/new')

def show(request, id):
    if request.method == "POST":
        validations = User.objects.validator(request.POST)
        if len(validations) == 0:
            user = User.objects.get(id=id)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return redirect('/users/'+id)
        else:
            print validations
            for error in validations:
                messages.add_message(request, messages.INFO, error)
                return redirect('/users/'+id+'/edit')
    else:
        user = User.objects.get(id=id)
        return render(request, 'restful_users/show.html', {'user':user})

def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'restful_users/edit.html', {'user': user})

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/users")
