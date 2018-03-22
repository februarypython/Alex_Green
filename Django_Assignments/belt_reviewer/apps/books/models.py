# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..beltreviewer.models import *
from django.db import models

# Create your models here.
#book table, title

class BookManager(models.Manager):
    def bookValidation(self, postData):
        errors = []
        title = postData['title']
        author = postData['author']
        new_author = postData['newauthor']
        review = postData['review']
        rating = postData['rating']
        book_check = Book.objects.filter(title=title, author=author)|Book.objects.filter(title=title, author=new_author)  
        if len(book_check) > 0:
            errors.append("This book already exists")
        if len(review) < 10:
            errors.append("Review must be at least 10 characters")
        if len(title) < 1:
            errors.append("Title is too short")
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    review = models.TextField()
    book = models.ForeignKey(Book, related_name="book_reviews")
    user = models.ForeignKey(User, related_name="user_reviews")
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



#author table. many to many w/ books ? do i need an author table or just put author in book model? lets try the latter first

#review table. one to many w/ books & one to many w/ users