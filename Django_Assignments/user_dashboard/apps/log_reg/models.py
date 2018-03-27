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
            user = self.create(
                    first_name=postData['first_name'],
                    last_name=postData['last_name'],
                    email=postData['email'],
                    password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                )
        return errors, user


class User(models.Model):
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
