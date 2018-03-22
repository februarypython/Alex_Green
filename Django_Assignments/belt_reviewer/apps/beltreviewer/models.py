# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData): 
        errors = []
        if len(postData['name']) < 2 or not postData['name'].isalpha():
            errors.append("Name must be atleast 2 characters, letters only")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email is not valid")
        if postData['password'] != postData['pwconfirm']:
            errors.append("Password and confirm must match")
        if len(postData['password']) < 8:
            errors.append("Password must be atleast 8 characters")
        if len(postData['alias']) < 1:
            errors.append("Must have an alias")
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return "name {} alias {}".format(self.name, self.alias)
    
#users table
#name, alias, email, pw, confirm

#user manager for validations

