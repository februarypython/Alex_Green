# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Description(models.Model): #one to one key
    description = models.TextField(default="")
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True,)
    
    def __str__(self):
        return self.description
