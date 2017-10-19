from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        for field, value in postData.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is reqired".format(field.replace('_', ' '))

            if len(postData['name']) < 5:
                errors["name"] = "Course name needs more than 5 character"
            if len(postData['desc']) < 15:
                errors['desc'] = "Description needs more than 15 character"
            
            return errors; 

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
         return "<Course object name: {}>".format(self.name)