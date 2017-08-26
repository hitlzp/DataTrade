# -*- coding: utf-8 -*-
from django.db import models

class news(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default = '')
    date = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    author = models.CharField(max_length=20)
