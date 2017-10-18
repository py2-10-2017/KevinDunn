from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return "<Course object name: {}>".format(self.name)