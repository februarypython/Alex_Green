# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = []
        user = None

        if len(postData['first_name']) < 1 or len(postData['last_name']) < 1:
            errors.append("Names must exist")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email is not valid")
        if postData['password'] != postData['pwconfirm']:
            errors.append("Password and confirm must match")
        if self.filter(email__iexact = postData['email']):
            errors.append("This email already exists in our database.")
        if len(postData['password']) < 8:
            errors.append("Pass too short")

        if not errors:
            if len(User.objects.all()) > 0:
                user_level = 1
            else:
                user_level = 9
            user = self.create(
                    first_name=postData['first_name'],
                    last_name=postData['last_name'],
                    email=postData['email'],
                    user_level=user_level,
                    password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                )
        return errors, user

    def validateLogin(self, postData):
        errors = []
        user = None

        try:
            user = self.get(email__iexact = postData['email'])
            pw = user.password
            if bcrypt.checkpw(postData['password'].encode(), pw.encode()) == True:
                return errors, user
            else:
                errors.append("Invalid login")
        except:
            errors.append("Invalid login")
        
        return errors, user
    
    def validateEditInfo(self, postData, id): #more email validation needed
        user = User.objects.get(id=id)
        errors = []
        if len(postData['first_name']) < 1 or len(postData['last_name']) < 1:
            errors.append("Names must exist")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Email is not valid")          
        if not errors:
            user.first_name = postData['first_name']
            user.last_name = postData['last_name']
            user.email = postData['email']
            user.save()
            print "successful changes"
        try:
            user.user_level=postData['user_level']
            user.save()
        except:
            pass
        return errors
    
    def validateEditPassword(self, postData, id): #inprogress
        user = User.objects.get(id=id)
        errors = []
        if postData['password'] != postData['pwconfirm']:
            errors.append("Password and confirm must match")
        if len(postData['password']) < 8:
            errors.append("Pass too short")
        if not errors:
            user.password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user.save()
            print user.password
            print "successfull password change"        
        return errors
    
        



class User(models.Model):
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.TextField()
    description = models.TextField(default="")
    user_level = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
