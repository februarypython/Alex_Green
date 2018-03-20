# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course, Description

# Create your views here.
def index(request):
    context = {
    "all_courses":Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    course = Course.objects.create(name=request.POST['course_name'])
    d1 = Description(course=course, description=request.POST['desc'])
    d1.save()
    return redirect("/")

def destroy(request, id):
    context = {
        "this_course":Course.objects.get(id=id)
    }
    return render(request, 'courses/remove.html', context)

def erase(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("/")

