# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Note
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    all_notes = Note.objects.all()
    context = {
        "all_notes": all_notes
    }
    return render(request, 'notes/index.html', context)

def process_note(request):
    Note.objects.create(
        title = request.POST['title'],
        note = request.POST['note']
    )
    return redirect("/")

def delete_note(request, id):
    Note.objects.get(id=id).delete()
    return redirect("/")
