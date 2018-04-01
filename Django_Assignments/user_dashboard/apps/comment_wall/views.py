# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request, id):
    if not 'user_id' in request.session:
        return redirect("/dashboard")
    else:
        context = {
            "user": User.objects.get(id=id),
            "user_messages": WallMessage.objects.filter(user_for=id),
            "user_comments": Comment.objects.all()
        }
        return render(request, "comment_wall/index.html", context)

def process_message(request, id):
    loggedin = request.session['user_id']
    validation = WallMessage.objects.validate(request.POST, id, loggedin)
    if len(validation) > 0:
        messages.add_message(request, messages.INFO, "message too short")
    return redirect("/profile/users/"+id)

def process_comment(request, messageid, id):
    loggedin = request.session['user_id']
    validation = Comment.objects.validate(request.POST, messageid, loggedin)
    if len(validation) > 0:
        messages.add_message(request, messages.INFO, "message too short")
    return redirect("/profile/users/"+id)