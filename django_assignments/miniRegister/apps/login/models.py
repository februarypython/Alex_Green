# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than 2 characters'.format(value)
        )

class User(models.Model):
    first_name = models.CharField(max_length=100, validators = [validateLengthGreaterThanTwo])
    last_name = models.CharField(max_length=100, validators = [validateLengthGreaterThanTwo])
    email = models.CharField(max_length=100, validators = [EmailValidator])
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
