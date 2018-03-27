# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def success(request):
    if not 'user' in request.session:
        return redirect("/")
    else:
        email = request.session['user']
        current_user = User.objects.get(email=email)
        reviews = Review.objects.all().order_by("-id")[:3]
        context = {
            "reviews": reviews,
            "user": current_user,
            "books": Book.objects.all()
            }    
        return render(request, 'books/success.html', context)
    

def view_book(request, id):
    if not 'user' in request.session:
        return redirect("/")
    else:
        book = Book.objects.get(id=id)
        email = request.session['user']
        current_user = User.objects.get(email=email)
        context = {
            'book':book,
            'user': current_user
        }
        return render(request, 'books/view_book.html', context)

def add_book_review(request):
    if not 'user' in request.session:
        return redirect("/")
    else:
        email = request.session['user']
        current_user = User.objects.get(email=email)   
        books = Book.objects.all()
        context = {
            "user": current_user,
            "books": books
        }
        return render(request, 'books/add_book_review.html', context)

def process_new_review(request):
    validations = Book.objects.bookValidation(request.POST)
    email = request.session['user']
    current_user = User.objects.get(email=email)
    title = request.POST['title']
    author = request.POST['author']
    new_author = request.POST['newauthor']
    review = request.POST['review']
    rating = request.POST['rating']
    if len(validations) == 0:        
        if len(author) < 1:
            print "less than 1======"
            b1 = Book.objects.create(title = title, author = new_author)
            Review.objects.create(review = review,book = b1,user = current_user,rating = rating)
            id = b1.id
            return redirect('/books/'+str(id))
        else:
            print "more than 1======="
            b1 = Book.objects.create(
            title = title,
            author = author
            )
            Review.objects.create(
            review = review,
            book = b1,
            user = current_user,
            rating = rating
            )
            id = b1.id
            return redirect('/books/'+str(id))        
    else:
        for error in validations:
            messages.add_message(request, messages.INFO, error)
            print error
        return redirect("/books/add")
    
def delete_review(request, id):
    Review.objects.get(id=id).delete()
    return redirect('/books/success')

def add_review_only(request, id):
    book = Book.objects.get(id=id)
    email = request.session['user']
    current_user = User.objects.get(email=email) 
    Review.objects.create(
        review = request.POST['review'],
        book = book,
        user = current_user,
        rating = request.POST['rating']
    )
    id = book.id
    return redirect('/books/'+str(id))

def user_info(request, id):
    if not 'user' in request.session:
        return redirect("/")
    else:
        context = {
            'user': User.objects.get(id=id),
            'rev': Review.objects.filter(user__id = id).count(),
            'all_books': Review.objects.filter(user__id=id)
        }  
    return render(request, 'beltreviewer/user_info.html', context)


    