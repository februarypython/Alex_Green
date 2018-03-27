# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'posts/index.html')

def process_post(request):
    new_post = Post.objects.create(post=request.POST['post_it'])
    context = {
        "new_post": new_post
    }
    return render(request, "posts/partial_post.html", context)

