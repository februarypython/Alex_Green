# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-15 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_author_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
