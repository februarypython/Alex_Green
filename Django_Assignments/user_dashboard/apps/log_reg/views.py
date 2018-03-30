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
            if User.objects.get(id=validation[1].id).user_level == 9:
                return redirect("/add_user")
            else:
                return redirect("/register")
    else:
        if not 'user_id' in request.session:
            request.session['user_id'] = validation[1].id
        if User.objects.get(id=validation[1].id).user_level == 9:
            return redirect("/dashboard/admin")
        else:
            return redirect("/dashboard")

def process_sign_in(request):
    validation = User.objects.validateLogin(request.POST)
    if len(validation[0]) < 1:
        request.session['user_id'] = validation[1].id
        if User.objects.get(id=validation[1].id).user_level == 9:
            return redirect("/dashboard/admin")
        elif User.objects.get(id=validation[1].id).user_level ==1:
            # request.session['user_id'] = validation[1].id
            return redirect("/dashboard")
    else:
        messages.add_message(request, messages.INFO, "Invalid Login")
        return redirect("/sign_in")

def dashboard_admin(request):
    if not 'user_id' in request.session:
        return redirect("/")
    if User.objects.get(id=request.session['user_id']).user_level == 9:
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "all_users": User.objects.all()
        }
        return render(request, 'log_reg/admin.html', context)
    else: 
        return redirect("/dashboard")

def dashboard(request):
    if not 'user_id' in request.session:
        return redirect("/")
    else:
        context = {
            "this_user": User.objects.get(id=request.session['user_id']),
            "all_users": User.objects.all()
        }
        print context
        if User.objects.get(id=request.session['user_id']).user_level == 9:
            return redirect("/dashboard/admin")
        else:
            return render(request, 'log_reg/dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect("/")

def add_user(request):
    if User.objects.get(id=request.session['user_id']).user_level == 9:
        return render(request, 'log_reg/add_user.html')
    else:
        return redirect("/dashboard")

def edit_self(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, 'log_reg/edit_self.html', context)

def update_user(request, id):
    # user = User.objects.get(id=id)
    if request.POST['edit_user'] == "user_info":
        validation = User.objects.validateEditInfo(request.POST, id)
        if len(validation) > 0:
            print validation
            messages.add_message(request, messages.INFO, "invalid info")
            return redirect("/users/"+id+"/edit")
        else:
            return redirect("/dashboard")

    if request.POST['edit_user'] == "user_password":
        validation = User.objects.validateEditPassword(request.POST, id)
        if len(validation) > 0:
            print validation
            print "invalid password"
            messages.add_message(request, messages.INFO, "pass too short")
            return redirect("/users/"+id+"/edit")
        else:
            return redirect("/dashboard")
       
            
    if request.POST['edit_user'] == "user_description":
        user.description = request.POST['description']
        user.save()
        return redirect("/dashboard")

def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/dashboard/admin")

def admin_edit_user(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render (request, 'log_reg/admin_edit_user.html', context)

def process_admin_edit(request, id):
    if request.POST['admin_edit'] == "edit_info":
        validation = User.objects.validateEditInfo(request.POST, id)
        if len(validation) > 0:
            print validation
            messages.add_message(request, messages.INFO, "invalid info")
            return redirect("admin/users/"+id+"/edit")
        else:
            return redirect("/dashboard/admin")
    if request.POST['admin_edit'] == "edit_password":
        validation = User.objects.validateEditPassword(request.POST, id)
        if len(validation) > 0:
            print validation
            messages.add_message(request, messages.INFO, "invalid password")
            return redirect("admin/users/"+id+"/edit")
        else:
            return redirect("/dashboard/admin")


