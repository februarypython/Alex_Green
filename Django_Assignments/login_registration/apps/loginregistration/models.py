# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = []
        if len(postData['first_name']) < 2:
            errors.append("First name is too short")
        if not postData['first_name'].isalpha(): #may need to be in str format. We'll seeee. update: nope
            errors.append("First name can only contain letters")
        if len(postData['last_name']) < 2:
            errors.append("Last name is too short")
        if not postData['last_name'].isalpha():
            errors.append("Last name can only contain letters")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email address is not valid")
        if len(postData['password']) < 8:
            errors.append("Password must be 8+ characters")
        if postData['password'] != postData['pwconfirm']:
            errors.append("Password and confirmed password must match")
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 

