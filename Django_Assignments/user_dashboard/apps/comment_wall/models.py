# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..user_dashboard/models import *
from django.db import models

# Create your models here.

class WallMessage(models.Model):
    wall_message = models.TextField()
    user = models.ForeignKey(User, related_name="wall_messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    wall_message = models.ForeignKey(WallMessage, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

