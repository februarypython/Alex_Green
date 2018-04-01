# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..log_reg.models import *
from django.db import models

#Create your models here.
class validateMessage(models.Manager):
    def validate(self, postData, id, loggedin):
        errors = []
        if len(postData['message']) < 3:
            errors.append("message must be longer")
        if not errors:
            WallMessage.objects.create(
                wall_message = postData['message'],
                user_for = User.objects.get(id=id),
                user_from = User.objects.get(id=loggedin)
            )
        return errors

class validateComment(models.Manager):
    def validate(self, postData, messageid, loggedin):
        errors = []
        if len(postData['comment']) < 2:
            errors.append("comment is too short")
        if not errors:
            Comment.objects.create(
                comment = postData['comment'],
                user_from = User.objects.get(id=loggedin),
                wall_message = WallMessage.objects.get(id=messageid)
            )
        return errors

class WallMessage(models.Model):
    wall_message = models.TextField()
    user_for = models.ForeignKey(User, null=True, related_name="messages_for", on_delete=models.CASCADE)
    user_from = models.ForeignKey(User, null=True, related_name="messages_from", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = validateMessage()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user_from = models.ForeignKey(User, null=True, related_name="comments_from", on_delete=models.CASCADE)
    wall_message = models.ForeignKey(WallMessage, null=True, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = validateComment()

