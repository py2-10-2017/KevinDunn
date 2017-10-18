from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        for field, value in postData.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is reqired".format(field.replace('_', ' '))

            if len(postData['first_name']) < 1:
                errors["first_name"] = "First name needs more than 1 character"
            if len(postData['last_name']) < 1:
                errors['last_name'] = "Last name needs more than 1 character"
            if len(postData['email']) < 5:
                errors['last_name'] = "Need a valid email"
            
            return errors; 

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
         return "<Blog object: {} {}>".format(self.first_name, self.last_name)